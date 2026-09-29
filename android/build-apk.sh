#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 sync_game.py
python3 tests/check_wrapper.py
if ! command -v gradle >/dev/null 2>&1; then
  echo '未找到 Gradle。请用 Android Studio 打开本目录并配置 Android SDK 35，再执行 assembleDebug。' >&2
  exit 2
fi
if [ -z "${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}" ]; then
  echo '未找到 ANDROID_HOME / ANDROID_SDK_ROOT。请先安装 Android SDK 35。' >&2
  exit 2
fi
gradle --no-daemon :app:assembleDebug
test -s app/build/outputs/apk/debug/app-debug.apk
echo "APK: $(pwd)/app/build/outputs/apk/debug/app-debug.apk"
