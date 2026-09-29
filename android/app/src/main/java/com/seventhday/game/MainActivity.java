package com.seventhday.game;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import java.io.ByteArrayInputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/** Offline WebView shell for the exact V0.4 game HTML. No INTERNET permission. */
public final class MainActivity extends Activity {
    private static final String GAME_URL = "https://appassets.androidplatform.net/assets/SeventhDay.html";
    private static final int PICK_SAVE = 101;
    private static final int WRITE_SAVE = 102;
    private WebView webView;
    private ValueCallback<Uri[]> fileCallback;
    private String pendingExport;

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState != null) pendingExport = savedInstanceState.getString("pendingExport");
        webView = new WebView(this);
        WebView.setWebContentsDebuggingEnabled(false);
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(false);
        settings.setAllowContentAccess(true); // Android document picker URI only.
        settings.setAllowFileAccessFromFileURLs(false);
        settings.setAllowUniversalAccessFromFileURLs(false);
        settings.setMediaPlaybackRequiresUserGesture(true);
        settings.setJavaScriptCanOpenWindowsAutomatically(false);
        settings.setSupportMultipleWindows(false);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_NEVER_ALLOW);
        settings.setDefaultTextEncodingName("UTF-8");
        webView.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                return !GAME_URL.equals(request.getUrl().toString());
            }
            @Override public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
                if (GAME_URL.equals(request.getUrl().toString())) {
                    try { return new WebResourceResponse("text/html", "UTF-8", getAssets().open("SeventhDay.html")); }
                    catch (Exception ignored) { return blocked(); }
                }
                return blocked(); // No external page, script, image or network request.
            }
            private WebResourceResponse blocked() {
                return new WebResourceResponse("text/plain", "UTF-8",
                    new ByteArrayInputStream(new byte[0]));
            }
        });
        webView.setWebChromeClient(new WebChromeClient() {
            @Override public boolean onShowFileChooser(WebView view, ValueCallback<Uri[]> callback,
                                                        FileChooserParams params) {
                if (fileCallback != null) fileCallback.onReceiveValue(null);
                fileCallback = callback;
                Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                intent.setType("*/*");
                intent.putExtra(Intent.EXTRA_MIME_TYPES,
                    new String[]{"application/json", "text/plain", "application/octet-stream"});
                try { startActivityForResult(intent, PICK_SAVE); }
                catch (Exception ex) { fileCallback.onReceiveValue(null); fileCallback = null; notifyUser("没有可用的文件选择器"); }
                return true;
            }
        });
        // Bridge only exists in the packaged local page. All other requests are blocked.
        webView.addJavascriptInterface(new GameBridge(), "AndroidBridge");
        setContentView(webView);
        webView.loadUrl(GAME_URL);
    }

    private final class GameBridge {
        @JavascriptInterface public void saveJson(String json) {
            if (json == null || json.length() > 100000) return;
            runOnUiThread(() -> {
                pendingExport = json;
                Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                intent.setType("application/json");
                intent.putExtra(Intent.EXTRA_TITLE, "seventh-day-save.json");
                try { startActivityForResult(intent, WRITE_SAVE); }
                catch (Exception ex) { pendingExport = null; notifyUser("没有可用的保存位置"); }
            });
        }
    }

    @Override protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_SAVE) {
            if (fileCallback != null) {
                Uri uri = resultCode == RESULT_OK && data != null ? data.getData() : null;
                fileCallback.onReceiveValue(uri == null ? null : new Uri[]{uri});
                fileCallback = null;
            }
        } else if (requestCode == WRITE_SAVE) {
            if (resultCode == RESULT_OK && data != null && data.getData() != null && pendingExport != null) {
                try (OutputStream out = getContentResolver().openOutputStream(data.getData())) {
                    if (out == null) throw new IllegalStateException("No output stream");
                    out.write(pendingExport.getBytes(StandardCharsets.UTF_8));
                    notifyUser("存档已导出");
                } catch (Exception ex) { notifyUser("保存失败，请重试"); }
            }
            pendingExport = null;
        }
    }

    @Override protected void onSaveInstanceState(Bundle outState) {
        outState.putString("pendingExport", pendingExport);
        super.onSaveInstanceState(outState);
    }
    @Override protected void onPause() { if (webView != null) webView.onPause(); super.onPause(); }
    @Override protected void onResume() { super.onResume(); if (webView != null) webView.onResume(); }
    @Override protected void onDestroy() {
        if (fileCallback != null) { fileCallback.onReceiveValue(null); fileCallback = null; }
        if (webView != null) { webView.removeJavascriptInterface("AndroidBridge"); webView.destroy(); webView = null; }
        super.onDestroy();
    }
    private void notifyUser(String text) { Toast.makeText(this, text, Toast.LENGTH_SHORT).show(); }
}
