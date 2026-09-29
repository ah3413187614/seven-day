# 七日全节点策划（DESIGNER_ONLY）

## d1_start · 第七声钟响之前

召集令钉在家门上，雨水洇黑了“勇者”两个字。七天后，封印将崩塌。送信人留下王国的赏格，又把教会的祝福念了一遍，便催马去了下一家。

托马蹲下来，把修桥的锤子塞进工具箱。河上的木板昨夜冲走了三块，村里已经有人把行李搬到岸边。他没有劝你留下，也没有替你收拾远行的包袱。

天亮后，王都、圣堂和旧林各有一班同行的人。工具箱放在第四条路上。

前置：开始游戏

### d1_start_1 · 带着故乡的粮单，响应王都召集。

当下理解：你得到入城凭证，同时接受：村里的青壮少了一个。

实际后果：你得到入城凭证；村里的青壮少了一个。

下一节点：d2_c；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["answered_summons"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日进入c起始路线。"}`

### d1_start_2 · 去圣辉教会，核对预言中被抹去的人名。

当下理解：你得到抄经人的席位，同时接受：教会登记了你的家乡。

实际后果：你得到抄经人的席位；教会登记了你的家乡。

下一节点：d2_h；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["sought_prophecy"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日进入h起始路线。"}`

### d1_start_3 · 进入精灵旧林，寻找黎明留下的剑痕。

当下理解：你避开王国征召，同时接受：熟悉的道路也到此为止。

实际后果：你避开王国征召；熟悉的道路也到此为止。

下一节点：d2_w；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["entered_forest"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日进入w起始路线。"}`

### d1_start_4 · 拒绝召集，留下修复故乡的渡桥。

当下理解：老人今晚仍有人照看，同时接受：召集令上你的名字被划去。

实际后果：老人今晚仍有人照看；召集令上你的名字被划去。

下一节点：d2_v；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["refused_summons"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日进入v起始路线。"}`

## d2_c · 粮单与冠冕

城门外的粮车排到了桥头。骑士玛伦替你作保，守卫才肯收下故乡的粮单。书吏把它压进一摞阵亡通知，纸角露出的村名正被雨水慢慢泡开。

摄政莱娅许诺今天发粮。她指向广场空着的台阶：那里需要一个接受封号的人。账房里，三座村庄已经从运输表上划去，改成了“暂缓”。门外有人端着空碗等答复。

前置：d1_start_1

### d2_c_1 · 签下征召誓书，换取故乡的粮车。

当下理解：粮车出发，同时接受：你须接受王庭征用。

实际后果：粮车出发；你须接受王庭征用。

下一节点：d3_c_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["obeyed_kingdom"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_c_2 · 留下核对军粮账，暂缓出征。

当下理解：找到虚报数字，同时接受：玛伦独自赶往前线。

实际后果：找到虚报数字；玛伦独自赶往前线。

下一节点：d3_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["audited_grain"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_c_3 · 当众读出被放弃的村名，逼王庭答复。

当下理解：城外难民得到听证，同时接受：粮车被扣作证物。

实际后果：城外难民得到听证；粮车被扣作证物。

下一节点：d3_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["challenged_crown"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_c_4 · 拿担保书护送难民，放弃受封。

当下理解：难民获准过门，同时接受：你的勇者席位由别人接替。

实际后果：难民获准过门；你的勇者席位由别人接替。

下一节点：d3_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["escorted_refugees"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d2_h · 钟楼下的删文

第六声钟响后，执事扶着钟轴，等了很久。修女伊芙翻开值夜记录，前几次封印失稳的日期旁，也都画着同样的缺口。

你的预言抄本缺了一页，断线夹在书脊里。院外的人要烧死一名带角的小信使；院内，医师正在给两族伤兵换药。同一首圣歌从两边传来。教皇瑟文站在走廊中央，手里握着钟楼和收容所的两串钥匙。

前置：d1_start_2

### d2_h_1 · 接下夜祷誓约，以服从换取进入钟楼。

当下理解：你获准接近封印仪表，同时接受：不能公开所见。

实际后果：你获准接近封印仪表；不能公开所见。

下一节点：d3_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["obeyed_church"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_h_2 · 替修女抄完病历，交换被删的书页。

当下理解：找到历代勇者同样的病症，同时接受：错过公开听证。

实际后果：找到历代勇者同样的病症；错过公开听证。

下一节点：d3_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["read_forbidden"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_h_3 · 把魔族信使带到广场，要求公开审理。

当下理解：信使妮娅暂免火刑，同时接受：你被记为争议证人。

实际后果：信使妮娅暂免火刑；你被记为争议证人。

下一节点：d3_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 2, "Church": -1}, "add_flags": ["saved_demon_child"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d2_h_4 · 关上收容所大门，同时收留两族伤兵。

当下理解：伤兵免受围攻，同时接受：医院粮票被暂时冻结。

实际后果：伤兵免受围攻；医院粮票被暂时冻结。

下一节点：d3_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["opened_shelter"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d2_w · 没有守卫的剑

旧林的路牌都朝着来处。地图师缇尔拨开藤蔓，露出最后一条还能辨认的刻线：“出去的路先记好。里面没有人替你带路。”

断裂的祭坛上，一柄剑裹着旧布。布边靠近你的手时，指尖忽然传来灼痛，眼前只闪过一片白光。缇尔按住你的肩，等你自己松开或握紧。

山下升起猎人的炉烟。更深的林子里，有什么东西正在敲一枚薄壳。

前置：d1_start_3

### d2_w_1 · 以性命作证，拔出圣剑黎明。

当下理解：黎明接受你的信念，同时接受：封印开始把痛觉传给你。

实际后果：黎明接受你的信念；封印开始把痛觉传给你。

下一节点：d3_w_oath；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["took_holy_sword"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_w_2 · 放下剑柄，测绘祭坛下的古代管道。

当下理解：你看见能量流向，同时接受：试炼资格不再保留。

实际后果：你看见能量流向；试炼资格不再保留。

下一节点：d3_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["refused_holy_sword"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_w_3 · 夺走猎人的熔炉芯，用它打开禁林。

当下理解：你取得不受教会控制的火，同时接受：猎人冬季生计被毁。

实际后果：你取得不受教会控制的火；猎人冬季生计被毁。

下一节点：d3_w_revolt；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["stole_furnace"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_w_4 · 先转移龙卵，把寻剑的时间让出去。

当下理解：幼龙离开猎场，同时接受：另一名求剑者进入祭坛。

实际后果：幼龙离开猎场；另一名求剑者进入祭坛。

下一节点：d3_w_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["protected_egg"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d2_v · 桥只够过一辆车

河水从桥墩缺口里冲过去，一辆车停在桥头，后面的车再也挪不动。村长托马把锤子递来，问明早能让几辆过去。

驻军要拆桥挡住斥候，船工却还在往桥下搬病人。魔族孩子妮娅拿来一张湿透的上游图，守卫看见她的角，先把图推了回去。她没有走，蹲在岸边，用石子重新摆出决堤的位置。

车上的老人敲了敲栏板。他还没来得及问，去的是哪一岸。

前置：d1_start_4

### d2_v_1 · 接受临时民兵印，带人守住桥头。

当下理解：村里有了警戒队，同时接受：孩子们开始叫你长官。

实际后果：村里有了警戒队；孩子们开始叫你长官。

下一节点：d3_v_oath；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["formed_militia"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d2_v_2 · 征用自己的屋梁，加固渡船并登记乘客。

当下理解：病人可以夜渡，同时接受：你的家再也挡不住雨。

实际后果：病人可以夜渡；你的家再也挡不住雨。

下一节点：d3_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["built_ferry"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_v_3 · 带家人从山路撤离，把工具留给村长。

当下理解：家人离开交战区，同时接受：其他村民仍在等待。

实际后果：家人离开交战区；其他村民仍在等待。

下一节点：d3_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["fled_village"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d2_v_4 · 留下照看走不了的人，让年轻人先走。

当下理解：无人被独自遗弃，同时接受：你失去白天撤离的机会。

实际后果：无人被独自遗弃；你失去白天撤离的机会。

下一节点：d3_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["stayed_with_weak"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d3_c_oath · 印玺的背面

玛伦把征马令推到桌边，印玺旁留好了签名的位置。粮车的辕折了一根，下一批粮必须在入夜前送到防线；院里的士兵已经牵来了各村最后能走的马。

单子背面粘着一封求救信。写信人没求免税，只求留一匹母马，春天还要耕田。玛伦揭了两次，纸没有分开。她便把整张单子翻过来，等你看完。

前置：d2_c_1

### d3_c_oath_1 · 签征马令，亲自跟随粮队承担责问。

当下理解：粮队能赶上防线，同时接受：村民失去春耕牲口。

实际后果：粮队能赶上防线；村民失去春耕牲口。

下一节点：d4_c_oath；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["requisitioned_horses"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_oath_2 · 把王令交给修女，请她核查征用名单。

当下理解：军需接受外部审计，同时接受：王庭不再独信你。

实际后果：军需接受外部审计；王庭不再独信你。

下一节点：d4_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["shared_writ"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_oath_3 · 烧掉征用单，让每户自行决定是否出马。

当下理解：农户保住选择权，同时接受：军粮晚到一夜。

实际后果：农户保住选择权；军粮晚到一夜。

下一节点：d4_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["burned_order"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_oath_4 · 用自己的军饷雇船，不让士兵进村。

当下理解：粮食沿河前行，同时接受：你没有钱购买护身药。

实际后果：粮食沿河前行；你没有钱购买护身药。

下一节点：d4_v_ledger；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["paid_transport"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_c_ledger · 账外的冬粮

奥伦打开地窖，里面没有金子，只有发霉的空粮袋。他把运输账摊在膝上，一项项指给你看：伪造的军粮去了一座不在王国名册里的麻风村。

同一批车也替人运军情。奥伦收过钱，账上留下了收款人的缩写，却不肯说谁雇了车。门边等领药的妇人不认识那些字母，只认得每旬会来的车铃。

前置：d2_c_2

### d3_c_ledger_1 · 封存全部账目，要求公开听证。

当下理解：贪腐无法隐去，同时接受：麻风村失去秘密供给。

实际后果：贪腐无法隐去；麻风村失去秘密供给。

下一节点：d4_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["published_accounts"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_ledger_2 · 保留救济支出，只追查军情买家。

当下理解：追查方向变窄，同时接受：你必须替部分假账担责。

实际后果：追查方向变窄；你必须替部分假账担责。

下一节点：d4_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["separated_accounts"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_ledger_3 · 接管运输线，用情报收入养活病人。

当下理解：救济继续，同时接受：走私者开始称你东家。

实际后果：救济继续；走私者开始称你东家。

下一节点：d4_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["lied_for_power"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_ledger_4 · 送出自己的行粮，再押奥伦去教会作证。

当下理解：证人和病人都有退路，同时接受：你将空腹赶路。

实际后果：证人和病人都有退路；你将空腹赶路。

下一节点：d4_h_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["protected_witness"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_c_revolt · 广场没有屋顶

广场挤得看不见石缝。弩手登上城门时，最先敲钟的工匠维克还站在钟绳下面，一名孩子被人群推到了他身旁。

莱娅派人送来会谈条件：交出敲钟者，弩手便撤。维克把孩子交给邻人，伸出了手腕，却不肯在认罪书上按印。来使把墨垫又往前挪了一寸。粮仓的锁仍挂着，人群开始拍门。

前置：d2_c_3

### d3_c_revolt_1 · 陪工匠入狱，用自己换一场正式听证。

当下理解：弩手撤离，同时接受：你接受教会监视。

实际后果：弩手撤离；你接受教会监视。

下一节点：d4_h_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Church": 1, "Companions": 1}, "add_flags": ["shared_sentence"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_revolt_2 · 抢占钟楼，迫使摄政交出粮仓钥匙。

当下理解：粮仓立刻开门，同时接受：守卫在冲突中受伤。

实际后果：粮仓立刻开门；守卫在冲突中受伤。

下一节点：d4_c_revolt；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"People": 1}, "add_flags": ["seized_bell"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_revolt_3 · 带人退出广场，把听证搬到难民营。

当下理解：孩子离开射程，同时接受：你的声势迅速减弱。

实际后果：孩子离开射程；你的声势迅速减弱。

下一节点：d4_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["deescalated_square"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_revolt_4 · 接受密谈，用不公开账目换三日粮食。

当下理解：饥民吃上饭，同时接受：工匠不再相信你的透明承诺。

实际后果：饥民吃上饭；工匠不再相信你的透明承诺。

下一节点：d4_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["lied_for_good"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_c_guard · 车轮下面

车轮陷进泥里，押队的人从路旁拖出一个魔族少年。他背包里的地图画着防线，也画着上游已经漫水的营地。有人拿绳子绑住了他的手。

妮娅认出哥哥的笔迹，伸手去指图角的日期。士兵先把图收走，要按战时军法处置。少年说营地今夜就会淹，声音小得几乎被车轮盖住。队尾的老人还不知道车为什么停了。

前置：d2_c_4

### d3_c_guard_1 · 护送少年去教会，让双方共同验图。

当下理解：少年保住性命，同时接受：车队行程暴露给教会。

实际后果：少年保住性命；车队行程暴露给教会。

下一节点：d4_h_revolt；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Demons": 2, "Church": -1}, "add_flags": ["saved_demon_child"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_guard_2 · 按军法处死持图者，立即转移防线。

当下理解：地图不再外传，同时接受：一名未受审的少年死去。

实际后果：地图不再外传；一名未受审的少年死去。

下一节点：d4_c_oath；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"Kingdom": 1, "People": -2, "Companions": -1}, "add_flags": ["killed_demon_child"], "remove_flags": [], "arc_tags": ["reason", "harm"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_guard_3 · 跟少年绕往上游，亲自验证洪水消息。

当下理解：能确认危险，同时接受：车队暂失你的保护。

实际后果：能确认危险；车队暂失你的保护。

下一节点：d4_w_ledger；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["verified_warning"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_c_guard_4 · 让玛伦押人，自己带老弱走另一条路。

当下理解：老人继续前进，同时接受：你放弃替少年决定命运。

实际后果：老人继续前进；你放弃替少年决定命运。

下一节点：d4_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["split_convoy"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d3_h_oath · 誓词里的空位

钟楼仪表的长卷落到了地上。最新一行数字与七百年前的记录接在一起，中间没有空白；伊芙摸过纸上的凸点，说这是心跳。卷边注明“活体承压”，每次脉冲都与心跳同步。

瑟文请你向楼下宣读神迹，好让各教区服从同一份撤离令。书吏已经写好颂词，留在窗边等签名。你问纸上是谁的心跳，瑟文没有回答，只把那份撤离地图铺得更平。

前置：d2_h_1

### d3_h_oath_1 · 宣读神迹，争取教会统一撤离命令。

当下理解：教区接受调度，同时接受：谎言由你亲口延续。

实际后果：教区接受调度；谎言由你亲口延续。

下一节点：d4_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["lied_for_good"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_oath_2 · 只公布心跳数据，暂不解释它属于谁。

当下理解：学者可以复核，同时接受：民间开始出现相反传言。

实际后果：学者可以复核；民间开始出现相反传言。

下一节点：d4_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["published_measurement"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_oath_3 · 拒绝宣读，把原卷交给魔族学者。

当下理解：另一方获得证据，同时接受：教会撤销你的通行证。

实际后果：另一方获得证据；教会撤销你的通行证。

下一节点：d4_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["rejected_church"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_oath_4 · 请求守在仪表旁，分担一次封印脉冲。

当下理解：陌生人的痛苦减轻，同时接受：你的手留下黑纹。

实际后果：陌生人的痛苦减轻；你的手留下黑纹。

下一节点：d4_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["shared_burden"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_h_ledger · 同一张病历

七份病历的纸色不同，伤口图却几乎重合。伊芙把一粒从魔族士兵伤口里取出的黑砂放上去，砂粒停在勇者画像胸前的银管旁。

页码跳过两处，删文批条盖着教会印。门外有人来收异端证据。伊芙没把病历合上，先拿布盖住了病人的名字。王庭工匠的地址写在她袖口，通往旧林的门在身后。钥匙转动之前，这些纸还来得及被带走。

前置：d2_h_2

### d3_h_ledger_1 · 把病历交给王庭工匠，要求盲审。

当下理解：获得独立测量，同时接受：病人的秘密离开医院。

实际后果：获得独立测量；病人的秘密离开医院。

下一节点：d4_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["cross_checked_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_ledger_2 · 将病历藏入自己的衣衬，独自查旧林。

当下理解：证据不被没收，同时接受：伊芙可能受你牵连。

实际后果：证据不被没收；伊芙可能受你牵连。

下一节点：d4_w_ledger；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["hid_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_ledger_3 · 签名承认抄本归你，保护伊芙留下。

当下理解：医院保住医师，同时接受：你承担异端指控。

实际后果：医院保住医师；你承担异端指控。

下一节点：d4_h_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["shielded_eve"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_ledger_4 · 以病历要挟执事，换取封印室钥匙。

当下理解：你得到门钥，同时接受：教会记住这笔债。

实际后果：你得到门钥；教会记住这笔债。

下一节点：d4_h_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Church": 1}, "add_flags": ["blackmailed_clergy"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_h_revolt · 证人的舌头

妮娅念到山道位置时停住了。瓦尔将军用指节叩了叩桌子，说那里还有平民，坐标不能交给人类。抄写员的笔悬在纸上，墨滴落进了一个村名。

你问山道还运什么，瓦尔把粮车清单递过来，底下却压着军用铆钉的收据。妮娅把自己的证词拉回面前。她能念出每一个字，也听得见门外谁在等这些字。

前置：d2_h_3

### d3_h_revolt_1 · 保留完整证词，允许双方观察员到场。

当下理解：证言更可信，同时接受：山道居民必须连夜搬迁。

实际后果：证言更可信；山道居民必须连夜搬迁。

下一节点：d4_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["open_testimony"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_revolt_2 · 删去坐标，只公开平民撤离的事实。

当下理解：居民位置保密，同时接受：证词留下可被攻击的缺口。

实际后果：居民位置保密；证词留下可被攻击的缺口。

下一节点：d4_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["lied_for_good"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_revolt_3 · 让妮娅自己决定，并陪她承担后果。

当下理解：她保有发言权，同时接受：你的阵营支持变得不确定。

实际后果：她保有发言权；你的阵营支持变得不确定。

下一节点：d4_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["respected_witness"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_revolt_4 · 拒绝军方条件，护送妮娅回魔族营地。

当下理解：孩子离开审讯，同时接受：公开审理无法完成。

实际后果：孩子离开审讯；公开审理无法完成。

下一节点：d4_w_guard；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["escorted_nia"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_h_guard · 一床两伤

止血药只剩一瓶。左床的军官握着撤离口令，右床的魔族工兵萨德画得出地下排水渠。伊芙把药放在两张床之间，没有替任何一边拉上帘子。

军官说先救他，门外的人就能通行。萨德没争，只用还能抬起的手补完图上一处断口。两条绷带都在渗血，药瓶上的刻度看得清清楚楚。

前置：d2_h_4

### d3_h_guard_1 · 先救军官，换取医院的通行口令。

当下理解：撤离手续可办，同时接受：工兵留下永久伤残。

实际后果：撤离手续可办；工兵留下永久伤残。

下一节点：d4_c_guard；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["saved_officer"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_guard_2 · 先救工兵，请他带伤员走地下渠道。

当下理解：排水渠可以启用，同时接受：军官失去一条腿。

实际后果：排水渠可以启用；军官失去一条腿。

下一节点：d4_w_ledger；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["saved_engineer"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_guard_3 · 稀释药物同时施救，接受两人的风险。

当下理解：两人都愿配合，同时接受：下一日医疗资源减少。

实际后果：两人都愿配合；下一日医疗资源减少。

下一节点：d4_h_guard；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_medicine"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_h_guard_4 · 献出自己的血，把整瓶药留作术后急救。

当下理解：两人暂时稳定，同时接受：你无法参加今晚的追捕。

实际后果：两人暂时稳定；你无法参加今晚的追捕。

下一节点：d4_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["gave_blood"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d3_w_oath · 剑没有宣判

猎人把盗粮者按在祭坛边。黎明发着热，猎人的棍子仍落了下去。缇尔抓住下一棒，问猎人肯不肯为自己饿着的女儿赴死。猎人点头，剑身的光没有暗。

祭坛账册上也记过相似的亮光，旁边却是一次屠村。缇尔翻到那页，没念下去。盗粮者蜷着身子，手里还攥着半块没有吃完的饼。

前置：d2_w_1

### d3_w_oath_1 · 立下供粮契约，请古龙担保双方停手。

当下理解：暴力暂止，同时接受：你必须偿还猎人的粮债。

实际后果：暴力暂止；你必须偿还猎人的粮债。

下一节点：d4_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["bound_dragon_pact"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_oath_2 · 交出自己的口粮，让盗粮者去王庭作证。

当下理解：囚犯免遭私刑，同时接受：你和缇尔将挨饿。

实际后果：囚犯免遭私刑；你和缇尔将挨饿。

下一节点：d4_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["fed_prisoner"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_oath_3 · 拔剑砍断猎人的武器，禁止私刑。

当下理解：盗粮者活下来，同时接受：猎人失去防身工具。

实际后果：盗粮者活下来；猎人失去防身工具。

下一节点：d4_w_revolt；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["stopped_lynching"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_oath_4 · 把剑暂寄祭坛，去查为何供粮中断。

当下理解：你获得账目线索，同时接受：暂时不能靠剑震慑。

实际后果：你获得账目线索；暂时不能靠剑震慑。

下一节点：d4_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["questioned_sword"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_w_ledger · 地下的河

教堂、王宫和龙巢的管线在山腹汇成一束。缇尔刮去铜管上的泥，里面仍有东西流动，检修铭文却被人逐字凿平。

检修门借着三处供能锁死。停下一处，门才能开。工匠把城里暖炉、圣灯和龙巢的位置标在图上，又在一旁画了一个接入活体的小孔。缇尔用布包住那个孔口，等你决定先动哪一边。

前置：d2_w_2

### d3_w_ledger_1 · 停王宫暖炉，进入主检修道。

当下理解：工匠得到入口，同时接受：宫中病人也将受冻。

实际后果：工匠得到入口；宫中病人也将受冻。

下一节点：d4_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["cut_palace_heat"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_ledger_2 · 借龙卵的余温供能，请龙族观察维修。

当下理解：检修不伤居民，同时接受：孵化被推迟。

实际后果：检修不伤居民；孵化被推迟。

下一节点：d4_w_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["borrowed_egg_heat"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_ledger_3 · 请求教会熄灭圣灯，记录一次完整波形。

当下理解：测量显示黑潮沿管道回流，活体负荷随支路泄压下降，同时接受：全城看见圣灯熄灭。

实际后果：测量显示黑潮沿管道回流，活体负荷随支路泄压下降；全城看见圣灯熄灭。

下一节点：d4_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["measured_abyss"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_ledger_4 · 用自己的生命火种启动旧机器。

当下理解：不用切断任何街区，同时接受：你开始咳血。

实际后果：不用切断任何街区；你开始咳血。

下一节点：d4_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["life_powered_machine"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_w_revolt · 被夺走的冬天

猎人追到断桥，把冻硬的手伸向炉芯。它的火足以破开龙鳞，余热也够山镇用过一个冬天。护送你的人把兵器横在桥上，没人先动。

猎人没有讨回整座炉子，只问女儿入冬以后怎么办。桥下能看见向王都去的运煤路，税卡还立着。炉芯里的灰轻轻撞击外壳，像有人从里面催促开门。

前置：d2_w_3

### d3_w_revolt_1 · 归还一半炉芯，凭残余力量继续前进。

当下理解：山镇得到供暖，同时接受：你失去强攻龙巢的把握。

实际后果：山镇得到供暖；你失去强攻龙巢的把握。

下一节点：d4_w_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["returned_heat"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_revolt_2 · 把炉芯献给王庭，换一队合法护卫。

当下理解：护卫归你调遣，同时接受：山镇要向王国买煤。

实际后果：护卫归你调遣；山镇要向王国买煤。

下一节点：d4_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["traded_furnace"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_revolt_3 · 邀请猎人入伙，让他共同决定炉芯用途。

当下理解：猎人愿意带路，同时接受：你不能独占力量。

实际后果：猎人愿意带路；你不能独占力量。

下一节点：d4_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_power"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_revolt_4 · 吞入炉芯灰烬，以自身替代燃料。

当下理解：力量留在你体内，同时接受：你开始听见陌生人的愿望。

实际后果：力量留在你体内；你开始听见陌生人的愿望。

下一节点：d4_w_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["ate_ash"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_w_guard · 巢外的契约

阿瑟兰伏在龙卵旁，爪尖压着一张村庄地图。它圈出附近的林地，说孵化需要热，火一旦失控，这几处屋顶都留不下。

缇尔把村民的取水路画上去，正穿过龙将要封锁的山口。古龙看了很久，没有把爪移开。卵壳又响了一声，山下送来的粮袋已经放在巢口，袋上缝着村里的姓氏。

前置：d2_w_4

### d3_w_guard_1 · 要求龙族先保护人类村庄，再谈孵化。

当下理解：互助条件明确，同时接受：古龙认为你缺乏敬意。

实际后果：互助条件明确；古龙认为你缺乏敬意。

下一节点：d4_v_oath；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["negotiated_dragon"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_guard_2 · 以自己的体温守卵，给村庄争取时间。

当下理解：无需点燃村庄，同时接受：你将错过一天休息。

实际后果：无需点燃村庄；你将错过一天休息。

下一节点：d4_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["warmed_egg"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_guard_3 · 拒绝预设牺牲，寻找另一处地热口。

当下理解：发现旧时代井道，同时接受：追捕者也会找到巢穴。

实际后果：发现旧时代井道；追捕者也会找到巢穴。

下一节点：d4_w_ledger；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["sought_third_heat"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_guard_4 · 答应缔约，但保留公开违约的权利。

当下理解：古龙承认你是谈判者，同时接受：关系从一条不信任开始。

实际后果：古龙承认你是谈判者；关系从一条不信任开始。

下一节点：d4_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["conditional_oath"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_v_oath · 长官的第一道命令

谷口两岸各亮着一盏灯。王国溃兵抬着担架，魔族侦察队举着水源图，谁都不肯先放下武器。桥板每次落脚都向下沉一点。

民兵把临时印交到你手里，问先接哪边。一名伤者的血滴进水中，下游的侦察兵已经开始搬高行李。桥边还剩一卷粗绳，够拆成两条索道；没人试过让它同时载这么多人。

前置：d2_v_1

### d3_v_oath_1 · 先接伤者，要求王国交出撤退地图。

当下理解：重伤者上岸，同时接受：魔族侦察队被困。

实际后果：重伤者上岸；魔族侦察队被困。

下一节点：d4_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["rescued_wounded"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_oath_2 · 先接侦察兵，交换下游全部水源坐标。

当下理解：几个村庄获救线索，同时接受：溃兵怀疑你的立场。

实际后果：几个村庄获救线索；溃兵怀疑你的立场。

下一节点：d4_h_revolt；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["traded_water_map"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_oath_3 · 带民兵分拆桥板，同时搭两条索道。

当下理解：两边都能开始过河，同时接受：民兵承担落水风险。

实际后果：两边都能开始过河；民兵承担落水风险。

下一节点：d4_v_ledger；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["built_two_crossings"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_oath_4 · 要求两军缴械混编，再一起过桥。

当下理解：桥头不再受军队控制，同时接受：你接下看守俘虏的责任。

实际后果：桥头不再受军队控制；你接下看守俘虏的责任。

下一节点：d4_v_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"People": 1}, "add_flags": ["disarmed_armies"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

## d3_v_ledger · 名单最后一行

托马称完最后一袋粮，在名单末尾写下载重。他划掉自己的名字，又把笔递给身旁的老人。老人将笔放回去：“我没有答应留在这里。”

船板低得快要贴住水面。妮娅在岸边标出一条林间小路，伤者却走不了那么远。快艇系在驻军哨所，修船的木料散在上游。第一阵大水已经带走了系船柱旁的土。

前置：d2_v_2

### d3_v_ledger_1 · 按伤情安排上船，自己带其余人走禁林。

当下理解：重伤者先行，同时接受：步行队面临迷路。

实际后果：重伤者先行；步行队面临迷路。

下一节点：d4_w_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["led_forest_evacuation"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_ledger_2 · 留下粮袋腾位置，渡河后向王庭求粮。

当下理解：所有乘客能上船，同时接受：明天必须找到粮食。

实际后果：所有乘客能上船；明天必须找到粮食。

下一节点：d4_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["dumped_supplies"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_ledger_3 · 征用驻军快艇，以村庄债券作抵押。

当下理解：运力足够，同时接受：故乡背上未来税债。

实际后果：运力足够；故乡背上未来税债。

下一节点：d4_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["issued_village_debt"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_ledger_4 · 留在岸上修第二条船，请托马领队。

当下理解：撤离可以继续，同时接受：你暂时和家人分开。

实际后果：撤离可以继续；你暂时和家人分开。

下一节点：d4_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["stayed_to_build"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d3_v_revolt · 山路朝着身后

安全领的烽火已经能看见了。家人在前面数着最后几级石阶，身后却传来桥钟，比约好的时刻早了三个时辰。

巡队停下来问是否有消息要带回去。你们剩的口粮装在同一只袋子里，离哨站还有一段路。家人攥着你的袖口，没有拉你往哪边走。第二声钟响时，巡队开始收紧马鞍。

前置：d2_v_3

### d3_v_revolt_1 · 送家人到哨站后折返桥头。

当下理解：家人安全，同时接受：你必须在黑夜独自赶路。

实际后果：家人安全；你必须在黑夜独自赶路。

下一节点：d4_v_oath；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["returned_after_flight"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_revolt_2 · 把口粮托给巡队，继续带家人前行。

当下理解：家人不再涉险，同时接受：你只能间接帮助故乡。

实际后果：家人不再涉险；你只能间接帮助故乡。

下一节点：d4_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["kept_fleeing"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_revolt_3 · 向教会报告钟声，请求开放避难所。

当下理解：救援获得坐标，同时接受：教会也取得你们的名册。

实际后果：救援获得坐标；教会也取得你们的名册。

下一节点：d4_h_guard；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"People": 1}, "add_flags": ["requested_sanctuary"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_revolt_4 · 去最近的龙井引水，为村庄争一夜。

当下理解：洪水推迟，同时接受：安全领的农田可能遭淹。

实际后果：洪水推迟；安全领的农田可能遭淹。

下一节点：d4_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["diverted_flood"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_v_guard · 留下的人

老人把炉边的位置让给了萨德。这个魔族工兵的腿还不能落地，手却能握住修桥的钉锤。他认得河上炸药的接法，也承认自己的队伍用过同样的东西。

巡逻队在门外要人，托马挡住了第一只伸进来的靴子。萨德把钉锤放回工具箱，说部队不会来接他。屋里的水已经烧开，药还没来得及煎。

前置：d2_v_4

### d3_v_guard_1 · 把萨德藏在地窖，请他帮忙修桥。

当下理解：桥有机会修好，同时接受：你的家成为军事目标。

实际后果：桥有机会修好；你的家成为军事目标。

下一节点：d4_h_revolt；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["sheltered_sad"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_guard_2 · 要求巡队签下不处决保证，再移交伤兵。

当下理解：村庄免于搜查，同时接受：你依赖一份脆弱的保证。

实际后果：村庄免于搜查；你依赖一份脆弱的保证。

下一节点：d4_c_guard；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["secured_trial"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_guard_3 · 以民兵代表身份拒绝搜屋。

当下理解：老人保有安宁，同时接受：你公开对抗驻军。

实际后果：老人保有安宁；你公开对抗驻军。

下一节点：d4_v_oath；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["defended_home"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d3_v_guard_4 · 随伤兵一起离开，把追兵引向旧林。

当下理解：村庄暂时脱险，同时接受：你失去守在家旁的机会。

实际后果：村庄暂时脱险；你失去守在家旁的机会。

下一节点：d4_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["drew_pursuit"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_c_oath · 王令以下的真相

莱娅从内柜取出继任诏书。勇者的名字后面留着死亡日期，下一任签名的位置与之紧挨着。另一张表把粮食和药材按“在任容器”列支，没有写魔王。

她指着父亲拒绝选拔的那一年，北岸三万人的死亡数写在页脚。窗外正有人等待下一道征用令。莱娅把印玺放到两张纸之间：“名单可以公开。人从哪里来？”

前置：d3_c_oath_1 / d3_c_ledger_3 / d3_c_guard_2 / d3_w_revolt_2 / d3_v_ledger_3

### d4_c_oath_1 · 接受候选容器的训练，要求撤离名单公开。

当下理解：你争到公开撤离，同时接受：王庭开始把你视为耗材。

实际后果：你争到公开撤离；王庭开始把你视为耗材。

下一节点：d5_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["accepted_training"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_oath_2 · 扣下诏书，召集工匠寻找替代方案。

当下理解：研究获得法律掩护，同时接受：传统继任被延误。

实际后果：研究获得法律掩护；传统继任被延误。

下一节点：d5_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["held_succession_record"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_oath_3 · 向广场承认真相，也承认你曾服从。

当下理解：谣言有了可核实的证人，同时接受：秩序短暂崩解。

实际后果：谣言有了可核实的证人；秩序短暂崩解。

下一节点：d5_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["confessed_lie"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_oath_4 · 先用王令迁走北岸居民，再追究王庭。

当下理解：更多人逃出危险区，同时接受：知情者获得销毁证据的时间。

实际后果：更多人逃出危险区；知情者获得销毁证据的时间。

下一节点：d5_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["evacuated_north"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_c_ledger · 并不存在的胜利

奥伦把庆功宴的账翻过去。下一页没有停战后的结清，只有送往魔王城的药材；相同的运费一路记到今年。

封印监测表附在新账后面，每次心跳异常，药量便增加一格。伊芙认出其中的止痛药，却不能凭药名说出病人是谁。车夫在门边等改道的地址。他今天要送的那一箱，还没有装车。

前置：d3_c_revolt_4 / d3_h_ledger_1 / d3_h_revolt_1 / d3_w_oath_4 / d3_v_ledger_2

### d4_c_ledger_1 · 保留药路，向王庭索要容器维修预算。

当下理解：旧容器得到药，同时接受：你接手维持谎言的账。

实际后果：旧容器得到药；你接手维持谎言的账。

下一节点：d5_c_oath；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["maintained_medicine"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_ledger_2 · 带一箱止痛药去见所谓魔王。

当下理解：会谈有了诚意，同时接受：人类护卫拒绝与你同行。

实际后果：会谈有了诚意；人类护卫拒绝与你同行。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["carried_medicine"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_ledger_3 · 复制运单交给各地医师，再毁掉原件坐标。

当下理解：真相不会被单方封存，同时接受：下一批送药需要改路。

实际后果：真相不会被单方封存；下一批送药需要改路。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["distributed_evidence"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_ledger_4 · 沿药路追踪深渊入口，亲自测量失控速度。

当下理解：得到现场数据，同时接受：你暴露在黑潮辐射下。

实际后果：得到现场数据；你暴露在黑潮辐射下。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["discovered_abyss"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_c_revolt · 胜利的口号

传单最末一行变成了“杀尽教士”。维克拿出原稿，那里原本只有调查日期。另一批印好的纸已经捆上推车，跑得快的孩子正在分发。

广场另一端，教士蹲在踩踏伤者身边包扎。人群有人认出了袍子上的纹章，拾起石块。维克拉住推车，印坊的工人却问他：到底谁有权决定下一张纸上印什么？

前置：d3_c_oath_3 / d3_c_ledger_1 / d3_c_revolt_2 / d3_w_ledger_1

### d4_c_revolt_1 · 挡住追打教士的人，承认运动已经伤人。

当下理解：受伤教士活下来，同时接受：激进派指责你背叛。

实际后果：受伤教士活下来；激进派指责你背叛。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["protected_clergy"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_revolt_2 · 接管印坊，所有传单先经你批准。

当下理解：煽动暂时停止，同时接受：言论重新需要许可。

实际后果：煽动暂时停止；言论重新需要许可。

下一节点：d5_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["controlled_press"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_revolt_3 · 让教皇公开回应原件，接受双向质询。

当下理解：双方证词被记录，同时接受：会谈消耗撤离时间。

实际后果：双方证词被记录；会谈消耗撤离时间。

下一节点：d5_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["held_public_hearing"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_revolt_4 · 带着愿同行的人离城，建立无王令的避难营。

当下理解：一部分人脱离冲突，同时接受：城里温和派失去组织者。

实际后果：一部分人脱离冲突；城里温和派失去组织者。

下一节点：d5_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["founded_free_camp"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_c_guard · 被救者的名字

玛伦带车队绕过旧王陵。避雨时，一名老人认出了壁画里年轻的勇者，说那张脸与魔王城药车上的病人画像一样。修复工剥下遮盖层，露出“艾德里安”的旧题名。

玛伦的下一道护送令仍写着讨伐，要把刚包扎好的伤员送进山腹。玛伦把姓名抄在担保书背面，车队已经收好了雨布。山口之外有去圣堂的岔路，留在这里的人正等她回来点名。

前置：d3_c_revolt_3 / d3_h_guard_1 / d3_w_oath_2 / d3_v_oath_1 / d3_v_guard_2

### d4_c_guard_1 · 取消讨伐护送，把伤员送往渡口。

当下理解：伤者不再赴死，同时接受：封印室缺少守卫。

实际后果：伤者不再赴死；封印室缺少守卫。

下一节点：d5_v_ledger；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["cancelled_hunt"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_guard_2 · 告诉玛伦真相，请她自愿带队护送药品。

当下理解：骑士获得选择权，同时接受：部分人当场离队。

实际后果：骑士获得选择权；部分人当场离队。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["trusted_maren"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_guard_3 · 暂不告诉全队，以救援名义继续向山腹走。

当下理解：队伍保持完整，同时接受：信任将来要由你偿还。

实际后果：队伍保持完整；信任将来要由你偿还。

下一节点：d5_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["lied_for_good"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_c_guard_4 · 独自去替伤员守住封印外门。

当下理解：伤员得到休息，同时接受：你承担第一轮深渊冲击。

实际后果：伤员得到休息；你承担第一轮深渊冲击。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["held_outer_gate"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_h_oath · 神谕的呼吸

祷词原件用小字写着“当事人可撤回同意”。后来的祭典本把这一行粘住，改成“奉献不可终止”。伊芙借灯照着纸背，旧字一点点透出来。

墙边传声管里响起答复，祭司的声音与机器杂音交叠。瑟文承认封条出自教会，说当年每一次交接都快赶不上崩塌。枢机在旁边递来新候选名单。纸上有手印，也有空白；瑟文没有再去接那支笔。

前置：d3_c_revolt_1 / d3_h_oath_1 / d3_h_ledger_4

### d4_h_oath_1 · 继续守誓，但要求誓词写明容器的同意权。

当下理解：信徒保留共同语言，同时接受：强制选拔受到约束。

实际后果：信徒保留共同语言；强制选拔受到约束。

下一节点：d5_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["reformed_oath"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_oath_2 · 拒绝替不明声音作证，将传声管公开封存。

当下理解：你保住诚实，同时接受：失去对祈祷仪式的控制。

实际后果：你保住诚实；失去对祈祷仪式的控制。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["faith_broken"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_oath_3 · 让学者、龙族与祭司共同辨认声音。

当下理解：学者用建造铭牌与权限表核对出曙母的分配来源，同时接受：各方争抢解释权。

实际后果：学者用建造铭牌与权限表核对出曙母的分配来源；各方争抢解释权。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["studied_oracle"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_oath_4 · 接替教皇承受一次回流，确认他是否说谎。

当下理解：你证实回流真实，同时接受：体内黑纹扩散。

实际后果：你证实回流真实；体内黑纹扩散。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["tested_burden"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_h_ledger · 七百年的同一个人

伊芙把勇者名册与病历并排放好。第一份签名是艾德里安，末页送药回执仍是同一个名字。画像上的冠饰被改过，耳后的伤疤没有。

装订线里夹着删去的交接记录，写明活人被接入封印，却没有提供替代方法。你可以抄走原件，也可以去问那个仍在签收药物的人。伊芙包好一只药箱，放在书旁。

前置：d3_c_oath_2 / d3_c_ledger_2 / d3_h_oath_2 / d3_w_ledger_3

### d4_h_ledger_1 · 公布完整原件，连同各方删改痕迹。

当下理解：任何阵营都难独占解释，同时接受：脆弱停火面临考验。

实际后果：任何阵营都难独占解释；脆弱停火面临考验。

下一节点：d5_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["published_original_record"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_ledger_2 · 将原件交给艾德里安，请他确认自己的意愿。

当下理解：旧勇者重新成为能回答的人，同时接受：你必须进入魔王城。

实际后果：旧勇者重新成为能回答的人；你必须进入魔王城。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["met_previous_hero"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_ledger_3 · 先研究他的病历，寻找容器以外的承压方式。

当下理解：找到分散承压的假说，同时接受：它还没有安全验证。

实际后果：找到分散承压的假说；它还没有安全验证。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["researched_lattice"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_ledger_4 · 封存原件，换取教会为伤员开仓。

当下理解：医院得粮，同时接受：真相暂时仍受权力保管。

实际后果：医院得粮；真相暂时仍受权力保管。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["bargained_archive"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_h_revolt · 魔王没有宝座

瓦尔带你穿过魔王城的病房。艾德里安坐在维修椅上，银管从衣领没入皮肤；门牌写着勇者旧名，病历上的年龄已经加了七百年。

他一口气只能说几句话，先请你把止痛管挪近些。墙上有历次交接时各族医师的签名。瓦尔递来一份战争誓书，艾德里安没有伸手。那张纸便一直悬在药杯上方。

前置：d3_c_guard_1 / d3_h_oath_3 / d3_v_oath_2 / d3_v_guard_1

### d4_h_revolt_1 · 陪他拒绝瓦尔的战争誓书。

当下理解：旧勇者不再孤立，同时接受：魔族军方撤走守卫。

实际后果：旧勇者不再孤立；魔族军方撤走守卫。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["reconciled_hero"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_revolt_2 · 先替他接上止痛管，再询问深渊结构。

当下理解：你得到清醒的证词，同时接受：输药消耗医院库存。

实际后果：你得到清醒的证词；输药消耗医院库存。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["discovered_abyss"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_revolt_3 · 接受他的一次记忆灌注，亲历首次封印。

当下理解：篡改的历史有了体验证据，同时接受：记忆可能侵蚀自我。

实际后果：篡改的历史有了体验证据；记忆可能侵蚀自我。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["received_memory"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_revolt_4 · 把瓦尔叫进来，要求他也为战争承担容器风险。

当下理解：将领不能只让别人付出，同时接受：谈判随时可能破裂。

实际后果：将领不能只让别人付出；谈判随时可能破裂。

下一节点：d5_c_revolt；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["challenged_warlord"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_h_guard · 医院里的魔王画像

伊芙给两张病床挪出了距离。军官指着萨德，说那座桥下有他的家人；萨德把另一张村庄名单压在被上，最上方印着教会的征讨章。

两人的伤口都需要换药，谁也没收回自己的话。墙上刚贴来的历史抄件无人去看。伊芙端来两盆清水，分别放下：“先说清楚，今天谁来领你们出院。”

前置：d3_c_ledger_4 / d3_h_ledger_3 / d3_h_revolt_2 / d3_h_guard_3 / d3_v_revolt_3

### d4_h_guard_1 · 建立共同病历，救治与追责分别进行。

当下理解：医院保住中立，同时接受：两边军方都嫌处理太慢。

实际后果：医院保住中立；两边军方都嫌处理太慢。

下一节点：d5_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["separated_care_trial"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_guard_2 · 请双方先互相指认失踪平民，寻找活人。

当下理解：复仇暂让位于救援，同时接受：受害者得不到即时惩罚。

实际后果：复仇暂让位于救援；受害者得不到即时惩罚。

下一节点：d5_v_ledger；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["listed_missing"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_guard_3 · 允许伤者拒绝和解，保证他们都能离院。

当下理解：个人边界得到尊重，同时接受：共同队伍可能瓦解。

实际后果：个人边界得到尊重；共同队伍可能瓦解。

下一节点：d5_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["refused_forced_peace"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_guard_4 · 替医院签下赔偿债，让双方先释放人质。

当下理解：人质获释，同时接受：你背下无法一人偿清的债。

实际后果：人质获释；你背下无法一人偿清的债。

下一节点：d5_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["assumed_reparation"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_w_oath · 黎明承认的怪物

阿瑟兰翻出两片留有剑痕的旧甲。一片属于艾德里安，另一片来自下令屠城的继任者，黎明在两个人手中都曾发光。

缇尔照着甲上的灼痕写下温度。古龙说，剑能认出肯付生命的意志，却不会查问那意志要带谁去死。祭坛上留着测试接口，不论你有没有带来那柄剑，记录都摆在面前。

前置：d3_h_oath_4 / d3_w_oath_1 / d3_w_ledger_4 / d3_w_guard_4

### d4_w_oath_1 · 给自己的用剑权加上同伴否决条款。

当下理解：同伴敢于劝阻，同时接受：战场决策变慢。

实际后果：同伴敢于劝阻；战场决策变慢。

下一节点：d5_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["limited_sword"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_oath_2 · 要求古龙教你承压，而不学习杀戮。

当下理解：容器训练开始，同时接受：你主动接近不可逆风险。

实际后果：容器训练开始；你主动接近不可逆风险。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["learned_containment"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_oath_3 · 将剑的性质告诉公众，拒绝天选者身份。

当下理解：人们能质疑持剑者，同时接受：联盟失去简单旗帜。

实际后果：人们能质疑持剑者；联盟失去简单旗帜。

下一节点：d5_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["rejected_chosen"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_oath_4 · 把剑接入测量阵列，验证它能否分散黑潮。

当下理解：得到关键实验，同时接受：武器暂时离手。

实际后果：得到关键实验；武器暂时离手。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["tested_sword_lattice"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_w_ledger · 龙骨是管道

墓道尽头的龙骨并没有安葬在土里，而是接进铜管。缇尔将波形贴在骨节旁，每一次黑潮回涨，骨管便向荒原排出一阵热雾。

旧契约写着，龙族同意把主要回流交给一个活人，以保住龙巢恒温。阿瑟兰的族印压在见证栏。工匠找到了可拆开的接头，出口另一端还有草地和水井，地图并不是空白。

前置：d3_c_guard_3 / d3_h_ledger_2 / d3_h_guard_2 / d3_w_guard_3 / d3_v_revolt_4

### d4_w_ledger_1 · 以测量证据要求龙族共同承担压力。

当下理解：龙族必须回应旧债，同时接受：谈判失去礼仪保护。

实际后果：龙族必须回应旧债；谈判失去礼仪保护。

下一节点：d5_w_guard；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["exposed_dragon_role"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_ledger_2 · 保留墓地秘密，交换完整的维修图。

当下理解：图纸到手，同时接受：你也成了隐瞒者。

实际后果：图纸到手；你也成了隐瞒者。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["kept_dragon_secret"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_ledger_3 · 把骨管接到无人荒原，做小规模试排。

当下理解：新方案取得数据，同时接受：荒原生态受到损伤。

实际后果：新方案取得数据；荒原生态受到损伤。

下一节点：d5_v_ledger；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["tested_empty_channel"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_ledger_4 · 拆取一段龙骨制造自己的承压器。

当下理解：你获得独立装备，同时接受：祖先遗骨受到冒犯。

实际后果：你获得独立装备；祖先遗骨受到冒犯。

下一节点：d5_w_revolt；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["took_dragon_bone"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_w_revolt · 力量的饥饿

两份地图都在营地的位置画了叉。瓦尔愿拿屠龙图换边防缺口，阿瑟兰愿替你烧掉魔族营地，换回被夺走的热源。

妮娅把平民的粮票铺到地图上，叉号下面至少住着二十户人。炉芯与黑潮试样隔着玻璃互相震动，工匠退开一步。古龙脱落的鳞片就在桌边，没人伸手去拿。

前置：d3_w_oath_3 / d3_w_revolt_4

### d4_w_revolt_1 · 拒绝两份交易，公布营地中的平民名单。

当下理解：双方借口失效，同时接受：你失去军力支持。

实际后果：双方借口失效；你失去军力支持。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["rejected_war_bargain"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_revolt_2 · 只取古龙脱落的鳞，放弃完整龙晶。

当下理解：古龙愿继续谈，同时接受：你的承压器功率受限。

实际后果：古龙愿继续谈；你的承压器功率受限。

下一节点：d5_w_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["spared_dragon"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_revolt_3 · 伏击古龙夺晶，将其余力量交给撤离队。

当下理解：撤离队得到强力屏障，同时接受：龙族不会遗忘这次杀戮。

实际后果：撤离队得到强力屏障；龙族不会遗忘这次杀戮。

下一节点：d5_c_guard；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Companions": 1, "Dragons": -4}, "add_flags": ["killed_dragon"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_revolt_4 · 用炉芯吸收黑潮试样，亲身查清代价。

当下理解：你取得难以复制的数据，同时接受：欲望开始带有别人的声音。

实际后果：你取得难以复制的数据；欲望开始带有别人的声音。

下一节点：d5_w_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["absorbed_abyss"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_w_guard · 幼龙也会燃烧

幼龙第一口火烧穿了围裙。送食物的村民把伤手浸在水里，仍能闻见焦布的味道。它缩到门后，尾巴抵着空食盆。

阿瑟兰答应付药钱，却要求病历不写龙族的名字。伊芙把空白病历递给伤者，没有替他落笔。缇尔搬来一桶水放在巢口，桶柄烫得还不能碰，今天的饭也还要有人送。

前置：d3_h_revolt_4 / d3_w_ledger_2 / d3_w_revolt_1 / d3_w_guard_2 / d3_v_ledger_1 / d3_v_guard_4

### d4_w_guard_1 · 要求公开道歉，把幼龙留在中立医院。

当下理解：伤者得到承认，同时接受：龙族的骄傲受损。

实际后果：伤者得到承认；龙族的骄傲受损。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["dragon_accountability"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_guard_2 · 替村民接受赔偿，隐去龙族责任。

当下理解：伤者立即获得药钱，同时接受：事实被你的签名掩盖。

实际后果：伤者立即获得药钱；事实被你的签名掩盖。

下一节点：d5_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["lied_for_good"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_guard_3 · 教幼龙自己道歉，拒绝替它决定一生。

当下理解：它学会停下火焰，同时接受：风险仍需社区承担。

实际后果：它学会停下火焰；风险仍需社区承担。

下一节点：d5_v_guard；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["raised_dragon"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_w_guard_4 · 让幼龙返回族群，自己留作赔偿人质。

当下理解：双方暂时不再争夺它，同时接受：你失去自由通行。

实际后果：双方暂时不再争夺它；你失去自由通行。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["became_hostage"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_v_oath · 没有被选中的人

托马从旧村志里找出一列修渠人的名字。最早出发的勇者排在第三个，前后的人继续轮班，领的都是同样的口粮。没有一页写过他们能替全村决定谁去送死。

民兵把新绘的封锁图压在村志上，等你圈出允许留下的人。门外有人问能不能先送孩子走。托马将名单转向众人，每个人都看得见自己的那一行。

前置：d3_w_revolt_3 / d3_w_guard_1 / d3_v_oath_4 / d3_v_revolt_1 / d3_v_guard_3

### d4_v_oath_1 · 成立轮值议事会，交出永久指挥权。

当下理解：民兵获得共同程序，同时接受：紧急决定不再只由你作出。

实际后果：民兵获得共同程序；紧急决定不再只由你作出。

下一节点：d5_v_ledger；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_command"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_oath_2 · 接受战时指挥，写下七日后的交权日期。

当下理解：调度集中，同时接受：交权承诺将受权力考验。

实际后果：调度集中；交权承诺将受权力考验。

下一节点：d5_c_oath；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["temporary_command"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_oath_3 · 训练两族伤兵守护撤离队。

当下理解：更多家庭获得护卫，同时接受：队内仇恨尚未消除。

实际后果：更多家庭获得护卫；队内仇恨尚未消除。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["mixed_guard"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_oath_4 · 亲自守在洪水缺口，让议事会继续开会。

当下理解：人们有时间商量，同时接受：你承受整夜水压。

实际后果：人们有时间商量；你承受整夜水压。

下一节点：d5_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["held_floodgate"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d4_v_ledger · 地图上的空白村

撤离图上，故乡和魔族河岸聚落都被涂成空地。维克沿着古渠往下量，发现这些空白正压在旧泄压口上；王都每少受一分压力，下游的水就会高一点。

渠中露出的龙骨接头连着山腹支路。两岸住户围着图，要工匠先把屋顶补回去。渠边还有一片你家的田，地势比房屋低。维克放下测尺，泥水已经漫过第一根标桩。

前置：d3_c_oath_4 / d3_v_oath_3

### d4_v_ledger_1 · 先登记所有空白村，再动工修渠。

当下理解：风险能被计算，同时接受：抢修时间变少。

实际后果：风险能被计算；抢修时间变少。

下一节点：d5_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["mapped_all_villages"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_ledger_2 · 向两岸居民说明代价，让他们共同表决。

当下理解：居民取得决定权，同时接受：有人坚持不迁。

实际后果：居民取得决定权；有人坚持不迁。

下一节点：d5_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["river_assembly"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_ledger_3 · 挖新旁路，让自己的农田承担第一轮排水。

当下理解：房屋暂时保住，同时接受：家人失去来年生计。

实际后果：房屋暂时保住；家人失去来年生计。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["gave_farmland"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_ledger_4 · 请求教会接纳拒迁的老人，逐户陪同搬走。

当下理解：老人不再独守，同时接受：医院空间更拥挤。

实际后果：老人不再独守；医院空间更拥挤。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["rescued_stayers"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_v_revolt · 安全领的关卡

安全领的守卫翻了两遍你的行李，要你交出沿路证词和旧友名单。他说查清谁与战争有关，才好放真正的平民进去。

墙内的灯亮着，墙外的孩子拿湿柴生火。守卫把入城章放在桌角，等你补写名字。你能听见故乡方向断续的钟声，却看不到那边发生了什么。空白纸被风吹到了你的鞋旁。

前置：d3_h_revolt_3 / d3_v_revolt_2

### d4_v_revolt_1 · 拒交旧友名单，在城外建立流民营。

当下理解：朋友免遭追查，同时接受：你失去城墙保护。

实际后果：朋友免遭追查；你失去城墙保护。

下一节点：d5_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["refused_informant"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_revolt_2 · 把灾情交给守卫，只保留无辜者的姓名。

当下理解：边境启动戒备，同时接受：报告不够完整。

实际后果：边境启动戒备；报告不够完整。

下一节点：d5_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["edited_border_report"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_revolt_3 · 把入城名额让给孩子，返回渡口。

当下理解：孩子获得安全，同时接受：你再次走向洪水。

实际后果：孩子获得安全；你再次走向洪水。

下一节点：d5_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["returned_for_others"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_revolt_4 · 接受临时劳役，以自己的工时换营地口粮。

当下理解：流民今晚能吃饭，同时接受：你失去行动时间。

实际后果：流民今晚能吃饭；你失去行动时间。

下一节点：d5_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["worked_for_refugees"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_v_guard · 家门里的旧王

地板下传来断续的敲击声。炉火忽然变蓝，一段陌生记忆闪过：一个年轻人提着湿透的鞋，站在修不好的门前。画面没有名字，托马也说不出那是谁。

井沿新落了黑砂，邻人端来的饭还冒着热气。托马找来纸，建议先记下听见的声音，再去请人辨认。门闩又松了，他把工具箱推到你脚边。

前置：d3_c_guard_4 / d3_h_guard_4 / d3_v_ledger_4

### d4_v_guard_1 · 把记忆写给教会，要求他们派人来解释。

当下理解：证词留下备份，同时接受：故乡进入官方视线。

实际后果：证词留下备份；故乡进入官方视线。

下一节点：d5_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["recorded_memory"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_guard_2 · 留在村里修门、做饭，组织彼此照料。

当下理解：恐惧没有压倒生活，同时接受：你错过一次权力会谈。

实际后果：恐惧没有压倒生活；你错过一次权力会谈。

下一节点：d5_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["kept_daily_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_guard_3 · 循记忆中的旧渠，去查山腹里是谁在传来回声。

当下理解：普通人也抵达魔王城，同时接受：故乡暂失你的主持。

实际后果：普通人也抵达魔王城；故乡暂失你的主持。

下一节点：d5_h_revolt；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["sought_previous_hero"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d4_v_guard_4 · 把家钥匙交给托马，承诺替故乡承担下一次脉冲。

当下理解：村民获得一夜平静，同时接受：你开始付出寿命。

实际后果：村民获得一夜平静；你开始付出寿命。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["offered_burden"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_c_oath · 王冠的抵押

摄政权的移交文书铺在桌上，旁边是下一任容器的候选名单。莱娅愿意交出印玺，却要有人在名单末尾签字，保证封印不会空着。

玛伦放下一封未签的辞职信。她问工程队还差多少铜线，莱娅把国库账翻到赤字那页。窗外的卫队仍按旧口令换岗，听不见屋里已经谈到了解散与继任。印泥刚刚添满。

前置：d4_c_ledger_1 / d4_c_revolt_2 / d4_v_oath_2

### d5_c_oath_1 · 接印，保留继任制度并增设志愿见证。

当下理解：命令立刻生效，同时接受：制度仍需要一个人受苦。

实际后果：命令立刻生效；制度仍需要一个人受苦。

下一节点：d6_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_oath_2 · 接印，把国库抵押给分压工程。

当下理解：工匠获得资源，同时接受：失败将让王国破产。

实际后果：工匠获得资源；失败将让王国破产。

下一节点：d6_c_ledger；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_oath_3 · 拒绝王冠，邀请莱娅以个人身份共同守门。

当下理解：她第一次没有官职掩护，同时接受：调度失去中央命令。

实际后果：她第一次没有官职掩护；调度失去中央命令。

下一节点：d6_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["refused_crown"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_oath_4 · 当众归还印玺，让撤离代表决定下一任。

当下理解：代表获得权力，同时接受：莱娅的忠军保持观望。

实际后果：代表获得权力；莱娅的忠军保持观望。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["refused_crown"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

## d5_c_ledger · 会算错的救命账

维克用炭笔圈出外环三个闸门。关闭它们，中央城区的压力便能降下来。奥伦取来户籍册，把三个街区的住户逐页夹进模型，两本册子都没有夹完。

工匠确认人还没撤净，闸门却不能一直敞开。桌下有一具备用承压器，银管短得只能接一个人。维克把标着误差的纸放在最上面，没再用手遮住。

前置：d4_c_oath_2 / d4_c_guard_3 / d4_w_guard_2 / d4_v_revolt_2

### d5_c_ledger_1 · 按模型关闭外环，抢救更多中央居民。

当下理解：中央屏障稳定，同时接受：外环有人来不及撤出。

实际后果：中央屏障稳定；外环有人来不及撤出。

下一节点：d6_c_oath；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"Kingdom": 1, "People": -2, "Companions": -1}, "add_flags": ["sacrificed_innocent"], "remove_flags": [], "arc_tags": ["reason", "harm"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_ledger_2 · 先撤空外环再关闭，接受中央失守风险。

当下理解：被当作数字的人获得时间，同时接受：核心压力继续上升。

实际后果：被当作数字的人获得时间；核心压力继续上升。

下一节点：d6_v_ledger；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["delayed_seal"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_ledger_3 · 把自己的承压器接进外环，替模型补上缺口。

当下理解：外环多出撤离窗口，同时接受：你的身体开始失控。

实际后果：外环多出撤离窗口；你的身体开始失控。

下一节点：d6_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["absorbed_overflow"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_ledger_4 · 公布模型误差，让各街区自行选择支路。

当下理解：居民知道真实风险，同时接受：方案不再统一。

实际后果：居民知道真实风险；方案不再统一。

下一节点：d6_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["published_uncertainty"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_c_revolt · 革命也要钥匙

粮仓开门后，第一批支持者要求领双份。旧配给官记得每个营地的人数，也认得站在门口的妇人——她额上的伤曾是他打的。

维克把钥匙交来，又回头看追随者的脸色。妇人没有抢钥匙，只要每天都能看见秤砣。粮袋堆到梁下，门口的队伍已经分成了几列，谁也不肯先退。

前置：d4_c_oath_3 / d4_h_ledger_1 / d4_h_revolt_4 / d4_w_oath_3

### d5_c_revolt_1 · 留任旧官员，由受害者监督每日配给。

当下理解：配给不必重建，同时接受：受害者需要再次面对施害者。

实际后果：配给不必重建；受害者需要再次面对施害者。

下一节点：d6_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["supervised_official"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_revolt_2 · 撤掉所有旧官员，亲自统管粮仓。

当下理解：旧势力退出，同时接受：分粮成了你的独占权。

实际后果：旧势力退出；分粮成了你的独占权。

下一节点：d6_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["centralized_power"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_revolt_3 · 让各营地轮派分粮员，放弃支持者特权。

当下理解：规则更平等，同时接受：一部分追随者离去。

实际后果：规则更平等；一部分追随者离去。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["abolished_privilege"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_revolt_4 · 先补给被抢过的家庭，自己人最后领取。

当下理解：早先伤害得到补偿，同时接受：盟友认为你偏袒外人。

实际后果：早先伤害得到补偿；盟友认为你偏袒外人。

下一节点：d6_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["repaired_movement_harm"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_c_guard · 玛伦没有拔剑

玛伦卸下剑，讲起当年烧毁的魔族哨站。她说点火令是自己下的，地下藏着平民；不是认错目标就能把这句话改掉。

瓦尔的停火条件里写着交人，撤离队却还在等她带路。玛伦把山口值岗图放在剑旁，说受审之前可以交接。图上最危险的闸口没有替班者，那一栏留着她的名字。

前置：d4_c_oath_4 / d4_h_guard_4 / d4_w_oath_1 / d4_w_revolt_3

### d5_c_guard_1 · 交她受双方共同审判，暂停她的指挥权。

当下理解：受害者得到程序，同时接受：队伍失去最熟练的骑士。

实际后果：受害者得到程序；队伍失去最熟练的骑士。

下一节点：d6_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["submitted_maren"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_guard_2 · 保她继续护送，但记录罪行并承诺战后追责。

当下理解：撤离保持战力，同时接受：正义被再次推迟。

实际后果：撤离保持战力；正义被再次推迟。

下一节点：d6_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["forgave_traitor"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_guard_3 · 拒绝用一个人换停火，护送她离开军队。

当下理解：她免遭筹码化，同时接受：瓦尔撤回停火提议。

实际后果：她免遭筹码化；瓦尔撤回停火提议。

下一节点：d6_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["protected_companion"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_c_guard_4 · 替她接下最危险的闸门，让她去受审。

当下理解：审判与救援可以同时进行，同时接受：你暴露在洪峰前。

实际后果：审判与救援可以同时进行；你暴露在洪峰前。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["took_maren_post"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_h_oath · 祭坛前的空椅

瑟文摘下教皇戒指，把自己写进志愿名单。枢机立刻端来权杖，请你接任；若无人答应，主张恢复强制选拔的主教已经准备好了仪式。

几名信徒来确认老人是不是被逼的。瑟文逐个回答，喉咙哑了，伊芙递给他水。他把候选名单推远了一点，先给最后一个还在犹豫的人留出说话的时间。

前置：d4_c_oath_1 / d4_h_oath_1

### d5_h_oath_1 · 接权杖，宣布一切承压必须出于知情同意。

当下理解：改革得到宗教权威，同时接受：仍有人自愿受苦。

实际后果：改革得到宗教权威；仍有人自愿受苦。

下一节点：d6_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_oath_2 · 拆分教皇职权，交给医师与地方教区。

当下理解：单人不再控制选拔，同时接受：决策要经过协商。

实际后果：单人不再控制选拔；决策要经过协商。

下一节点：d6_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["decentralized_church"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_oath_3 · 烧掉强制候选名单，请信徒自行离开。

当下理解：被选中的人重获自由，同时接受：继任储备骤减。

实际后果：被选中的人重获自由；继任储备骤减。

下一节点：d6_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["destroyed_candidate_list"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_oath_4 · 请瑟文留下照料信徒，由你参加承压。

当下理解：医院有了熟悉的主持者，同时接受：你承担他的风险。

实际后果：医院有了熟悉的主持者；你承担他的风险。

下一节点：d6_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["replaced_pope"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_h_ledger · 真相的使用说明

研究员把城市的抽取记录接上回流图：旧文明移走的疼痛在地下汇成海，又从裂口涌回来。停止抽取后，城里一间病房的麻醉先失了效。

另一份建造铭文称分配意志为“曙母”。它原本协调供能，后来取得了征用活人的权限。扬声器忽然问你要不要减轻痛苦。伊芙按住录音开关，没有替这声音写上神或机器。

前置：d4_c_revolt_3 / d4_h_guard_1 / d4_v_guard_1

### d5_h_ledger_1 · 保留分配意志，只删去强制征用权限。

当下理解：系统可继续工作，同时接受：没人保证它不会再次演变。

实际后果：系统可继续工作；没人保证它不会再次演变。

下一节点：d6_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["edited_mother_protocol"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_ledger_2 · 准备终止分配意志，让各地自行承压。

当下理解：强制神谕可能终结，同时接受：协调能力也将消失。

实际后果：强制神谕可能终结；协调能力也将消失。

下一节点：d6_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["prepared_deicide"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_ledger_3 · 接替它发布命令，让损失由自己决定。

当下理解：系统暂获明确指令，同时接受：你走向同一种专断。

实际后果：系统暂获明确指令；你走向同一种专断。

下一节点：d6_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["claimed_oracle"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_ledger_4 · 把回流疼痛传给自己，先叫停无同意抽取。

当下理解：居民不再被秘密抽取，同时接受：痛苦转入你的身体。

实际后果：居民不再被秘密抽取；痛苦转入你的身体。

下一节点：d6_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["stopped_extraction"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_h_revolt · 停火的刀鞘

瓦尔在停火书上添了“胜利”二字。道路可以今夜开放，平民的名字却要列在他的军旗之下。妮娅把改过的纸递回来，问失去家的人什么时候投过票。

外面第一辆运伤者的车已经套好马。再拖下去，夜里的口令就会更换。瓦尔扣押粮车的收据压在桌角，他看见了，却仍握着自己的笔。

前置：d4_c_ledger_2 / d4_c_guard_2 / d4_h_oath_2 / d4_h_ledger_2 / d4_h_revolt_1 / d4_w_revolt_1 / d4_v_guard_3

### d5_h_revolt_1 · 签临时停火，只承认通行而不承认胜利。

当下理解：道路暂时开放，同时接受：双方宣传仍互相冲突。

实际后果：道路暂时开放；双方宣传仍互相冲突。

下一节点：d6_h_guard；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["limited_truce"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_revolt_2 · 邀请两族平民代表另签救援公约。

当下理解：平民获得独立声音，同时接受：军事保护有所减弱。

实际后果：平民获得独立声音；军事保护有所减弱。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["civilian_pact"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_revolt_3 · 公开瓦尔扣押粮车的证据，逼其退让。

当下理解：军方的体面受损，同时接受：谈判可能变成武斗。

实际后果：军方的体面受损；谈判可能变成武斗。

下一节点：d6_c_revolt；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"People": 1}, "add_flags": ["exposed_var"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_revolt_4 · 用自己作为停火人质，换取无条件通道。

当下理解：人群开始通行，同时接受：你失去下一夜的自由。

实际后果：人群开始通行；你失去下一夜的自由。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["truce_hostage"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_h_guard · 医院不能成为国家

医院门外排起求判土地的人。伊芙听完一名伤者，拿出病历证明他受过枪伤；来人追问土地该还给谁，她把笔放下了。

药柜只剩两层，军队派人来问能否优先领取。另一边的家属开始搬病床，床脚卡在门槛上。等候的人给它让出一道缝，刚才争执的两个村名还留在登记簿里。

前置：d4_c_ledger_3 / d4_c_revolt_1 / d4_h_ledger_4 / d4_w_guard_1 / d4_v_oath_3 / d4_v_ledger_4 / d4_v_revolt_4

### d5_h_guard_1 · 建立证词档案，让医院只负责救治。

当下理解：伤害得到保存，同时接受：判决被延后。

实际后果：伤害得到保存；判决被延后。

下一节点：d6_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["founded_testimony_archive"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_guard_2 · 把医院改为跨族避难区，请所有军队缴械。

当下理解：伤者获得缓冲，同时接受：医院失去军方药品优先权。

实际后果：伤者获得缓冲；医院失去军方药品优先权。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["neutral_sanctuary"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_guard_3 · 让伊芙带伤员先走，自己抵押房产买药。

当下理解：药车能出发，同时接受：故乡不再有属于你的房子。

实际后果：药车能出发；故乡不再有属于你的房子。

下一节点：d6_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["sold_home_for_medicine"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d5_h_guard_4 · 将库存公开，由各病区共同分配。

当下理解：配药不再依靠关系，同时接受：争论耗费护理时间。

实际后果：配药不再依靠关系；争论耗费护理时间。

下一节点：d6_v_ledger；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["open_medicine_inventory"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_w_oath · 容器的同意

阿瑟兰让你先松开银管，等手指恢复知觉再继续。艾德里安的声音从相连的传声筒里传来，请求在下一次脉冲前停下。

医师念出他的病历与旧勇者姓名，记录了这次请求。立即交接需要新承压者，分流的图纸还在另一张桌上。古龙把两份表并排摆好，一份写着接替，一份写着等候；后者也需要艾德里安签名。

前置：d4_c_guard_4 / d4_h_oath_4 / d4_h_revolt_3 / d4_w_oath_2 / d4_w_ledger_2 / d4_w_guard_4 / d4_v_guard_4

### d5_w_oath_1 · 答应在第七日接替他，留下正式同意书。

当下理解：旧勇者看见休息的可能，同时接受：你的未来被承诺占据。

实际后果：旧勇者看见休息的可能；你的未来被承诺占据。

下一节点：d6_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["promised_succession"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_oath_2 · 请求他再坚持两夜，争取验证分流方案。

当下理解：研究获得时间，同时接受：痛苦仍由他承担。

实际后果：研究获得时间；痛苦仍由他承担。

下一节点：d6_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["asked_hero_wait"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_oath_3 · 尊重他立即停下的权利，亲自接住第一轮回流。

当下理解：他的呼吸第一次平稳，同时接受：你可能无法撑到天明。

实际后果：他的呼吸第一次平稳；你可能无法撑到天明。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["relieved_hero"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_oath_4 · 拒绝继任制度，邀请所有知情者参加自愿分压。

当下理解：责任不再只落于英雄，同时接受：共同方案缺乏经验。

实际后果：责任不再只落于英雄；共同方案缺乏经验。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["called_volunteers"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

## d5_w_ledger · 不能保证的第三条路

缇尔把城市供暖管接到试验支路。黑潮压力下降时，屋里的暖石一起冷了下去，刚拆掉的绷带又开始疼。工匠把这些也记入结果，没有只抄平稳的波形。

分散回流能减轻单一容器的负担，却要每处接入的人承担日常损耗。试验区旁还有备用接口，紧急时能重新锁住一个活人。缇尔把封条递来，问这道门该由谁保管。

前置：d4_c_ledger_4 / d4_h_oath_3 / d4_h_ledger_3 / d4_h_revolt_2 / d4_w_oath_4 / d4_v_ledger_3

### d5_w_ledger_1 · 完成小规模试验，保留失败时的容器接口。

当下理解：技术风险下降，同时接受：备用接口仍可被滥用。

实际后果：技术风险下降；备用接口仍可被滥用。

下一节点：d6_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["lattice_validated"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_ledger_2 · 公开图纸，让各城决定是否接入。

当下理解：无人被强迫承担，同时接受：系统覆盖不完整。

实际后果：无人被强迫承担；系统覆盖不完整。

下一节点：d6_v_ledger；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["open_lattice"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_ledger_3 · 用自己的承压器保护试验区居民。

当下理解：试验区风险下降，同时接受：你的身体损耗增加。

实际后果：试验区风险下降；你的身体损耗增加。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["shielded_test"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_ledger_4 · 删去安全限幅，换取一夜完成的全功率试验。

当下理解：获得强力数据，同时接受：试验场留下不可逆污染。

实际后果：获得强力数据；试验场留下不可逆污染。

下一节点：d6_w_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["overclocked_lattice"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_w_revolt · 下一次饥饿

临时承压器接在手腕，街边的争吵一响，表针便向上跳。一个声音从管里提出，只收陌生人的恐惧，与你同行的人可以不算。

送饭的人站在门口，不敢跨过那根管线。工匠留下一只控制盒，说锁扣交给别人也能打开。地穴在营外，没有住户，去那里切断供能就得自己承受反冲。饭在门槛边放凉了。

前置：d4_w_ledger_4 / d4_w_revolt_4

### d5_w_revolt_1 · 接受恐惧供能，要求它不得吞噬同伴。

当下理解：力量上升，同时接受：陌生人的痛苦成了代价。

实际后果：力量上升；陌生人的痛苦成了代价。

下一节点：d6_w_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"Dragons": 1, "People": -2, "Companions": -1}, "add_flags": ["fed_on_fear"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_revolt_2 · 交出承压器，请同伴限制你的力量。

当下理解：朋友可以靠近，同时接受：你暂时失去威慑。

实际后果：朋友可以靠近；你暂时失去威慑。

下一节点：d6_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["surrendered_power"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_revolt_3 · 把供能规则公之于众，只接受自愿贡献。

当下理解：人们能够拒绝，同时接受：战力变得不稳定。

实际后果：人们能够拒绝；战力变得不稳定。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["consensual_power"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_revolt_4 · 在无人的地穴自断回路，承担反噬。

当下理解：恐惧不再被抽取，同时接受：你的生命受损。

实际后果：恐惧不再被抽取；你的生命受损。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["broke_corruption"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_w_guard · 一枚卵的重量

阿瑟兰愿意加入分压，却把幼龙的名字从风险表里划去。村里的孩子仍在另一页上，照护人看过两张表，将笔停在半空。

古龙护着卵，没有争辩那两页是否公平。它问若先撤孩子，工程要推迟多久。缇尔拿来共同照护的名册，最前面一栏写的是谁能接孩子，后面才是种族。

前置：d4_w_ledger_1 / d4_w_revolt_2

### d5_w_guard_1 · 拒绝特权，让两族孩子都先撤出试验区。

当下理解：孩子被同等对待，同时接受：试验必须推迟。

实际后果：孩子被同等对待；试验必须推迟。

下一节点：d6_v_ledger；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["evacuated_children"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_guard_2 · 同意保护幼龙，换取古龙立即承压。

当下理解：封印得到支撑，同时接受：人类代表质疑双重标准。

实际后果：封印得到支撑；人类代表质疑双重标准。

下一节点：d6_w_oath；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["dragon_priority"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_guard_3 · 请求古龙把保护权交给两族共同照护会。

当下理解：跨族共同监护形成，同时接受：父亲失去单方决定权。

实际后果：跨族共同监护形成；父亲失去单方决定权。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1, "Dragons": 2}, "add_flags": ["shared_dragon_care"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_w_guard_4 · 自己留下守卵，请古龙去救河岸居民。

当下理解：河岸获得援手，同时接受：你承担孵化时的灼伤风险。

实际后果：河岸获得援手；你承担孵化时的灼伤风险。

下一节点：d6_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["exchanged_watch"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d5_v_oath · 平民的议事桌

议事会选你做代表，散会前却有人又坐下来，问能不能不去承压。另几个人愿意留下，但不认识接口上任何一个刻度。

托马把两份名单分开，空出退出者离开的通道。工程队送来训练时间表，王庭的征集表也送到了。两张纸都缺人签，院外的车只等到日落，车上的空水桶已经绑好。

前置：d4_v_ledger_2

### d5_v_oath_1 · 允许拒绝者撤离，余下的人自愿组队。

当下理解：合作出于同意，同时接受：劳力不足。

实际后果：合作出于同意；劳力不足。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["protected_refusal"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_oath_2 · 按技能分工，只让受训者靠近封印。

当下理解：意外风险下降，同时接受：未受训者认为自己被排除。

实际后果：意外风险下降；未受训者认为自己被排除。

下一节点：d6_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["trained_volunteers"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_oath_3 · 把代表席让给两族轮值，自己承担夜班。

当下理解：权力开始流动，同时接受：你无法主导所有决定。

实际后果：权力开始流动；你无法主导所有决定。

下一节点：d6_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["gave_up_seat"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_oath_4 · 以战时必要为由强制征集承压人员。

当下理解：工程人手齐备，同时接受：“志愿”失去了意义。

实际后果：工程人手齐备；“志愿”失去了意义。

下一节点：d6_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"Kingdom": 1, "People": -2, "Companions": -1}, "add_flags": ["forced_volunteers"], "remove_flags": [], "arc_tags": ["ambition", "harm"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_v_ledger · 最后一船工具

铜线捆在码头一侧，没走的住户坐在另一侧。船工摸过水位刻痕，说今晚只够稳稳地往返一次。萨德蹲在闸边，比着没有铜线时该怎样徒手修补。

收费门的木板比船舷厚，领主的封印钉在上面。住户开始收拾行李，却不知道该上船还是继续等。萨德卷起袖子，手指在冰冷的水里试了一下。

前置：d4_c_guard_1 / d4_h_guard_2 / d4_w_ledger_3 / d4_v_oath_1 / d4_v_ledger_1

### d5_v_ledger_1 · 先送住户，让萨德在安全处等待。

当下理解：居民撤出，同时接受：工程缺少材料。

实际后果：居民撤出；工程缺少材料。

下一节点：d6_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["people_before_tools"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_ledger_2 · 先送铜线，留下自己陪住户等回程。

当下理解：工程如期开工，同时接受：你和住户面临洪水。

实际后果：工程如期开工；你和住户面临洪水。

下一节点：d6_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["tools_before_people"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_ledger_3 · 拆掉渡口收费门，制成临时第二艘船。

当下理解：双方都能启程，同时接受：地方领主失去财产权。

实际后果：双方都能启程；地方领主失去财产权。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["broke_tollgate"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_ledger_4 · 请萨德主导手工修闸，自己承担水下工位。

当下理解：工具短缺得到缓解，同时接受：两人都有受伤风险。

实际后果：工具短缺得到缓解；两人都有受伤风险。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["worked_underwater"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_v_revolt · 自由的边界

城外营地借不到仓房，粮食仍装在每家的袋子里。一户人白天拒绝分粮，夜里抱来发烧的孩子，要借最后一包药。

有人把白天的争执又说了一遍，孩子却已咳得接不上气。你的口粮放在锅旁，吃完这一份，明天便得再找来源。远处王都的运输灯还亮着，回去的人需要先通过军队的盘查。

前置：d4_c_revolt_4 / d4_h_guard_3 / d4_v_revolt_1

### d5_v_revolt_1 · 允许拒绝分粮，同时公开所有求助与回应。

当下理解：个人选择保留，同时接受：互信要缓慢重建。

实际后果：个人选择保留；互信要缓慢重建。

下一节点：d6_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["kept_open_camp"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_revolt_2 · 建立最低互助契约，参加者共同分配。

当下理解：互助有了边界，同时接受：拒绝者仍可能挨饿。

实际后果：互助有了边界；拒绝者仍可能挨饿。

下一节点：d6_v_oath；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["mutual_aid_contract"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_revolt_3 · 把自己的份额交出去，不要求对方签字。

当下理解：孩子今晚吃饱，同时接受：你没有余粮应对明天。

实际后果：孩子今晚吃饱；你没有余粮应对明天。

下一节点：d6_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["unconditional_aid"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_revolt_4 · 返回王都争取物资，接受被通缉的风险。

当下理解：营地可能得到援助，同时接受：你重新进入权力范围。

实际后果：营地可能得到援助；你重新进入权力范围。

下一节点：d6_c_guard；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["returned_for_supply"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d5_v_guard · 门钥匙的去处

托马来问井里的黑砂怎么处理，家人来问今晚是否还要出门。两拨人等在同一扇门旁，谁也没有先开口催促。

新水提上来，桶底又有一层亮点。维修队愿意接手查管，医院在征轮值照护者，山闸仍少一个夜班。桌上的钥匙只有一把，给谁留下，都要先把话说完。水桶暂时留在门外。

前置：d4_w_guard_3 / d4_v_oath_4 / d4_v_revolt_3 / d4_v_guard_2

### d5_v_guard_1 · 留下修井，把研究交给懂它的人。

当下理解：村里有了安全水，同时接受：你放弃亲自控制终局。

实际后果：村里有了安全水；你放弃亲自控制终局。

下一节点：d6_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["trusted_specialists"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_guard_2 · 带家人一起参加撤离，不再替他们隐瞒危险。

当下理解：家人能够决定，同时接受：他们未必选择与你同行。

实际后果：家人能够决定；他们未必选择与你同行。

下一节点：d6_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["told_family_truth"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_guard_3 · 请托马照看家人，自己去守最后一道闸。

当下理解：故乡获得时间，同时接受：你可能不能回来取钥匙。

实际后果：故乡获得时间；你可能不能回来取钥匙。

下一节点：d6_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["left_key_home"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d5_v_guard_4 · 建立轮值照护，让每个家庭都能暂时休息。

当下理解：责任不再只由一户承担，同时接受：组织需要耗费体力。

实际后果：责任不再只由一户承担；组织需要耗费体力。

下一节点：d6_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_care"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_c_oath · 无人替你签字

莱娅在承压名单里添上自己的名字，印玺仍放在你这边。将军来问今晚的统一口令，工匠则要求切掉王宫的独立供能。

窗外的宫墙先闪了一次，廊下侍从开始搬走灯架。继任仪式和拒征者撤离都需要守卫，两队人正等在相反的门口。书吏把所有命令抄好，最下方只留了一个签名处。

前置：d5_c_ledger_1 / d5_c_revolt_2 / d5_h_ledger_3 / d5_v_oath_4

### d6_c_oath_1 · 亲自主持继任仪式，并写明退出权。

当下理解：仪式得以进行，同时接受：临阵退出仍可能危及全局。

实际后果：仪式得以进行；临阵退出仍可能危及全局。

下一节点：d7_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["consent_rite"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_oath_2 · 封闭王宫电路，把王冠能源交给工程队。

当下理解：分压工程获得余量，同时接受：王庭失去独立屏障。

实际后果：分压工程获得余量；王庭失去独立屏障。

下一节点：d7_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["released_crown_power"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_oath_3 · 留下御印统率卫队，承担终局的全部命令。

当下理解：部队仍然统一，同时接受：权力集中到你一人。

实际后果：部队仍然统一；权力集中到你一人。

下一节点：d7_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["kept_war_power"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_oath_4 · 解散强征名册，亲自护送拒绝者离城。

当下理解：被征者能够离开，同时接受：封印守卫减少。

实际后果：被征者能够离开；封印守卫减少。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["freed_conscripts"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_c_ledger · 误差栏的签名

最后一版模型附着龙骨支路的实测地址，管道从山腹通向各区泄压口；维克带你核对了最近一处，流向与记录相符。奥伦带来追加预算的批条，条件是删掉那一栏；维克将纸抽回来，又量了一次接头。

各区送来的同意书厚薄不一，有的只有负责人的签名。工程队能先开局部支路，也能继续等现场复核。桌边的承压器还留着空接口，渡口来人催问是否先让居民过河。

前置：d5_c_oath_2 / d5_c_revolt_1

### d6_c_ledger_1 · 保留误差，让各区按知情协议接入。

当下理解：居民承担明白的风险，同时接受：覆盖率低于理想值。

实际后果：居民承担明白的风险；覆盖率低于理想值。

下一节点：d7_c_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["shared_load"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_ledger_2 · 用军令强制接入，保证系统完整。

当下理解：模型接近最佳效率，同时接受：拒绝权消失。

实际后果：模型接近最佳效率；拒绝权消失。

下一节点：d7_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"Kingdom": 1, "People": -2, "Companions": -1}, "add_flags": ["forced_load"], "remove_flags": [], "arc_tags": ["ambition", "harm"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_ledger_3 · 把最危险的一路引向自己的承压器。

当下理解：试验有了缓冲，同时接受：你的生还机会下降。

实际后果：试验有了缓冲；你的生还机会下降。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["personal_buffer"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_ledger_4 · 暂停全域试验，先让人群通过渡口。

当下理解：即时伤亡风险下降，同时接受：系统只能争取短期稳定。

实际后果：即时伤亡风险下降；系统只能争取短期稳定。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["evacuation_first"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

## d6_c_revolt · 胜利之前的审判

天亮前处决旧官员的名单已经贴满广场。维克把斧头放在桌上，承认有几个名字只是抄错，却不愿为他们停下整场审判。

看守把证人的手也绑了起来。有人认出昨夜替营地送药的那个人，声音很快被口号盖住。档案车停在侧门，医院还缺人搬床，刑台正中则为你留着一把椅子。

前置：d5_c_ledger_4 / d5_h_revolt_3

### d6_c_revolt_1 · 拒绝集体处决，保护档案和证人。

当下理解：证据得以保存，同时接受：激进派准备夺权。

实际后果：证据得以保存；激进派准备夺权。

下一节点：d7_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["stopped_purge"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_revolt_2 · 接过斧头，以恐惧结束争执。

当下理解：广场暂时安静，同时接受：无辜者的死亡不能被撤回。

实际后果：广场暂时安静；无辜者的死亡不能被撤回。

下一节点：d7_c_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"People": -1, "Companions": -1}, "add_flags": ["killed_innocent"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_revolt_3 · 交还领导权，带反对屠杀的人去救伤者。

当下理解：一部分人离开暴力，同时接受：你失去政治控制。

实际后果：一部分人离开暴力；你失去政治控制。

下一节点：d7_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["renounced_purge_power"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_revolt_4 · 站在刑台上，要求先审判你自己的命令。

当下理解：问责不再只针对败者，同时接受：救援失去你的指挥。

实际后果：问责不再只针对败者；救援失去你的指挥。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["accepted_judgment"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_c_guard · 骑士的最后一班岗

山口的撤离队与审判队相遇，玛伦在两份名单上都被点到。双方没有握手，只把各自缺人的夜岗交换着看了一遍。

她收下新值班表，没有请你撤掉起诉书。下方的路仍可去封印室，坡上的伤者却走得越来越慢。值夜火盆熄了一只，玛伦蹲下添柴，等你安排下一班，火边还放着两双未干的靴子。

前置：d5_c_guard_2 / d5_w_revolt_2 / d5_v_revolt_4

### d6_c_guard_1 · 把护送权交给她，自己进封印室谈判。

当下理解：她承担公开职责，同时接受：你把后背交给有罪的人。

实际后果：她承担公开职责；你把后背交给有罪的人。

下一节点：d7_h_revolt；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["trusted_companion_again"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_guard_2 · 亲自守山口，让两边伤者先走。

当下理解：队伍争到时间，同时接受：你可能失去入城机会。

实际后果：队伍争到时间；你可能失去入城机会。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["last_rearguard"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_guard_3 · 公开轮值名单，拒绝任何阵营独占道路。

当下理解：道路成为共同设施，同时接受：军方优先权受限。

实际后果：道路成为共同设施；军方优先权受限。

下一节点：d7_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_road"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d6_c_guard_4 · 严格按速度分流，不为任何熟人插队。

当下理解：总撤离效率提高，同时接受：亲近的人也必须等待。

实际后果：总撤离效率提高；亲近的人也必须等待。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["equal_queue"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_h_oath · 没有赦罪的祝福

瑟文把权杖放在空椅上。来求赦罪的人问接过祝福后能否不用受审，他摇了摇头，替对方重新系好松开的绷带。

枢机催着统一今晚的祷词，门外信徒却在问是否可以退出候选。维修者拆开神谕装置，铭牌写着旧文明分配意志“曙母”。原始权限表列明，它曾从协调供能扩大到征用活人。瑟文留下灯，让每个人都能看清签过什么。

前置：d5_c_oath_1 / d5_h_oath_1 / d5_w_oath_1

### d6_h_oath_1 · 承认拒绝权，在公开见证下接过权杖。

当下理解：教会仍有共同仪式，同时接受：服从不再理所当然。

实际后果：教会仍有共同仪式；服从不再理所当然。

下一节点：d7_h_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["public_consent"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得守誓者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_oath_2 · 把忏悔与赔偿写入继任公约。

当下理解：旧罪留在记录里，同时接受：你失去无瑕的公众形象。

实际后果：旧罪留在记录里；你失去无瑕的公众形象。

下一节点：d7_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["reparation_covenant"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_oath_3 · 拆除神谕强制回路，将信仰留给个人。

当下理解：神谕不能再征用人，同时接受：各教区必须自己决定。

实际后果：神谕不能再征用人；各教区必须自己决定。

下一节点：d7_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["oracle_unbound"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_oath_4 · 把候选者全送出门，留下自己值守。

当下理解：没人被推上祭台，同时接受：你成为唯一的缓冲。

实际后果：没人被推上祭台；你成为唯一的缓冲。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["sole_volunteer"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_h_ledger · 曙母的第二个答案

分配意志从旧记录里读出你家乡的地址，提出给那里单独加一道屏障。代价栏列的是另一条街，街上的住户姓名被折在纸背。

伊芙把纸翻过来，启动征用的权限与旧建造铭文完全相同。扬声器问是否接受，机器外又传来一声无法追溯来源的叹息。录音还在转，工匠已经打开了接口盒。

前置：d5_c_guard_1 / d5_h_oath_2 / d5_h_guard_1

### d6_h_ledger_1 · 拒绝私人赦免，准备关闭强制分配核心。

当下理解：系统不再偏袒你，同时接受：私人愿望没有保证。

实际后果：系统不再偏袒你；私人愿望没有保证。

下一节点：d7_h_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Demons": 1}, "add_flags": ["refused_private_salvation"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得异端证人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_ledger_2 · 保留计算核心，建立任何人可退出的接口。

当下理解：社会仍可协调供能，同时接受：技术需要长期维护。

实际后果：社会仍可协调供能；技术需要长期维护。

下一节点：d7_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["built_exit_switch"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_ledger_3 · 接受交换，先保证自己的同伴存活。

当下理解：熟人得到屏障，同时接受：陌生街区承担压力。

实际后果：熟人得到屏障；陌生街区承担压力。

下一节点：d7_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"Kingdom": 1, "People": -2, "Companions": -3}, "add_flags": ["betrayed_strangers"], "remove_flags": [], "arc_tags": ["ambition", "harm"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_ledger_4 · 由自己承担它索要的份额，拒绝指定替身。

当下理解：无人替你支付，同时接受：你承担过量回流。

实际后果：无人替你支付；你承担过量回流。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["refused_substitute"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_h_revolt · 旧勇者请求睡眠

艾德里安把雨声认成了军靴，直到医师让他摸到窗沿的水。他确认了旧姓名，问约定的停止时间是否还算数。

银管仍在承担整座山腹的压力，松开一根都需要有人接手。两族医师在门外等见证，军队也带来了各自的旗。他请把旗放低一点，遮住了床边唯一能看见天的地方。

前置：d5_h_oath_3 / d5_h_ledger_2

### d6_h_revolt_1 · 和他约定交接时刻，不再把同意视为永久。

当下理解：旧勇者保有撤回权，同时接受：你必须兑现时间。

实际后果：旧勇者保有撤回权；你必须兑现时间。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["hero_consent_renewed"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_revolt_2 · 邀请两族医师留下见证他的决定。

当下理解：双方承认同一事实，同时接受：更多人接近危险核心。

实际后果：双方承认同一事实；更多人接近危险核心。

下一节点：d7_h_guard；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_witnesses"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_revolt_3 · 要求军队退出，以普通人的身份陪他等天亮。

当下理解：临终不再是战利品，同时接受：外部防护削弱。

实际后果：临终不再是战利品；外部防护削弱。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["dismissed_armies"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_revolt_4 · 接受残存记忆，承诺替他把被删的名字带出去。

当下理解：历史不再仅剩官方版本，同时接受：你的记忆也会受扰动。

实际后果：历史不再仅剩官方版本；你的记忆也会受扰动。

下一节点：d7_h_ledger；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Church": 1}, "add_flags": ["received_memory"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_h_guard · 最后的病房灯

伊芙将药柜的存量贴在门口，划掉已经用尽的两项。能走的人各自决定是否撤，留下的人把陪同者的名字写在床尾。

船工来量病床的宽度，军队的接管令随后送到。伊芙没有拆信，先替呼吸机换好最后一枚阀片。窗外的撤离灯正在一盏盏熄灭，屋里还剩这么多张床，床边的鞋尚未收起。

前置：d5_c_revolt_4 / d5_h_revolt_1 / d5_v_guard_4

### d6_h_guard_1 · 留下维持灯与呼吸机，让医师只管救治。

当下理解：重伤者继续得到照料，同时接受：你进入最后撤离批次。

实际后果：重伤者继续得到照料；你进入最后撤离批次。

下一节点：d7_h_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["kept_hospital_light"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_guard_2 · 把每张病床编入渡口计划，按伤情安排船位。

当下理解：转运变得可执行，同时接受：轻伤者必须步行。

实际后果：转运变得可执行；轻伤者必须步行。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["planned_bed_evacuation"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_guard_3 · 允许伤者选择自己的陪同者，不按种族分船。

当下理解：家庭不再被制度拆散，同时接受：部分船只载重不均。

实际后果：家庭不再被制度拆散；部分船只载重不均。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["kept_families_together"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_h_guard_4 · 把医院钥匙交给共同理事会，拒绝军队接管。

当下理解：医院保有中立，同时接受：将失去军队优先补给。

实际后果：医院保有中立；将失去军队优先补给。

下一节点：d7_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["civil_hospital"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

## d6_w_oath · 剑柄与扶手

封印椅的扶手已经调好，银管却还没扣上。古龙把继任书转向你，上面没有写王位，只列着疼痛、轮班和退出时需要的替代条件。

分流工程的信号从侧墙传来，隔一会儿便断一次。工匠带来一段备用管，必须先辨清回流方向才敢接入。椅旁还能站下几个人，门外也有人准备离开。

前置：d5_c_oath_3 / d5_c_ledger_3 / d5_h_oath_4 / d5_h_ledger_4 / d5_w_guard_2

### d6_w_oath_1 · 签下有限期继任书，要求继任者继续寻找替代。

当下理解：交接能够开始，同时接受：世界仍依赖一个身体。

实际后果：交接能够开始；世界仍依赖一个身体。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["finite_succession"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_oath_2 · 拆一段椅管接入分流，给工程最后一次机会。

当下理解：多一条替代通路，同时接受：交接稳定性下降。

实际后果：多一条替代通路；交接稳定性下降。

下一节点：d7_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["opened_backup_channel"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_oath_3 · 请求同伴带走黎明的故事，只把痛苦留给自己。

当下理解：同伴能够离开，同时接受：你可能不被后世记住。

实际后果：同伴能够离开；你可能不被后世记住。

下一节点：d7_w_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["erased_hero_credit"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_oath_4 · 拒绝独自承担，召集仍愿留下的平民。

当下理解：责任可被共同讨论，同时接受：黎明前的时间所剩无几。

实际后果：责任可被共同讨论；黎明前的时间所剩无几。

下一节点：d7_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["rejected_single_vessel"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

## d6_w_ledger · 试验要有人签名

缇尔把已完成的试验贴到左墙，缺少签名的区域贴到右墙。管道接回日常生活后，暖石会冷，病痛会回来，墙上没有写“免除代价”。

每个支路留着本地开关。工匠说，可以先运行有完整记录的部分，也可以用活体缓冲冒更大的险。装着龙晶的封箱还没获批准，红蜡完整地封在扣上。

前置：d5_h_ledger_1 / d5_w_oath_2 / d5_w_ledger_1 / d5_v_ledger_2

### d6_w_ledger_1 · 逐区确认同意，启动共同承压的预备网。

当下理解：分压准备完成，同时接受：覆盖仍取决于居民自愿。

实际后果：分压准备完成；覆盖仍取决于居民自愿。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_load"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_ledger_2 · 用自己的承压器做总缓冲，保留停机权。

当下理解：系统多一次试错，同时接受：风险集中到你身上。

实际后果：系统多一次试错；风险集中到你身上。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["personal_buffer"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_ledger_3 · 公开全部维修图，让拒绝接入者保留退路。

当下理解：技术不再由少数人垄断，同时接受：统一调度变难。

实际后果：技术不再由少数人垄断；统一调度变难。

下一节点：d7_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["open_lattice"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_ledger_4 · 接入未经批准的龙晶，强行提高功率。

当下理解：功率足以压制一轮黑潮，同时接受：龙晶被永久污染。

实际后果：功率足以压制一轮黑潮；龙晶被永久污染。

下一节点：d7_w_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["unlicensed_boost"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_w_revolt · 深渊懂得你的名字

临时回路把附近的惊叫一并传进耳朵，表针跟着跳。核心请你下命令，只需指定谁可以被计算，今夜的压力就能降下来。

同伴带来一副自毁锁，钥匙放在离你较远的桌角。另一侧是受影响街区寄来的姓名，有人要求永远封住接口。撤离队还在等最后一批供能，线缆从门缝里伸出去。

前置：d5_w_ledger_4 / d5_w_revolt_1

### d6_w_revolt_1 · 给力量套上自毁锁，请同伴保管钥匙。

当下理解：力量受到外部约束，同时接受：同伴背负终止你的责任。

实际后果：力量受到外部约束；同伴背负终止你的责任。

下一节点：d7_w_guard；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["power_kill_switch"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_revolt_2 · 吸尽周围恐惧，独占封印核心。

当下理解：一轮冲击被压住，同时接受：周围人失去宁静。

实际后果：一轮冲击被压住；周围人失去宁静。

下一节点：d7_w_revolt；终局身份：None

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"Dragons": 1, "People": -2, "Companions": -1}, "add_flags": ["claimed_abyss"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_revolt_3 · 向受害者交还控制权，接受被永久封禁。

当下理解：伤害有了制止方式，同时接受：你的行动受限。

实际后果：伤害有了制止方式；你的行动受限。

下一节点：d7_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["accepted_restraint"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_revolt_4 · 自断供能链，把最后的力量送给撤离队。

当下理解：撤离屏障增强，同时接受：你不再能靠力量自保。

实际后果：撤离屏障增强；你不再能靠力量自保。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["gave_last_power"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_w_guard · 天亮前的看守人

龙巢、医院与村庄各派来几名守门者。有人不识字，缇尔便把交班时辰画成月亮的位置，备用钥匙交到最年轻的那个人手中。

幼龙的箱子已经装车，护盾能拆成两部分，拆开后便不能完整罩住巢穴。炉火近乎熄灭，来人围着它伸出手。契约的最后一页仍空着，纸角被火光照得发红。

前置：d5_c_guard_4 / d5_h_revolt_4 / d5_w_oath_3 / d5_w_ledger_3 / d5_w_revolt_4 / d5_v_ledger_4 / d5_v_guard_3

### d6_w_guard_1 · 陪守门者轮值，不让任何人独撑到死。

当下理解：每人都有休息，同时接受：交接可能出现空隙。

实际后果：每人都有休息；交接可能出现空隙。

下一节点：d7_w_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["rotating_watch"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得护卵者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_guard_2 · 把龙巢护盾拆开，分别罩住病房与渡口。

当下理解：更多人得到短时保护，同时接受：龙巢失去完整屏障。

实际后果：更多人得到短时保护；龙巢失去完整屏障。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_dragon_shield"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_guard_3 · 让幼龙随难民走，自己守住将熄的炉火。

当下理解：幼龙离开危险区，同时接受：你留在回流前沿。

实际后果：幼龙离开危险区；你留在回流前沿。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["sent_egg_away"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_w_guard_4 · 邀请古龙与平民签共同守望契约。

当下理解：跨族合作得到承诺，同时接受：双方都必须放弃特权。

实际后果：跨族合作得到承诺；双方都必须放弃特权。

下一节点：d7_w_oath；终局身份：None

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {"Dragons": 2}, "add_flags": ["befriended_dragon"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_v_oath · 没有英雄的会议

议事会没有等你到场才开始。有人争论分流，有人点撤离人数，一个孩子抱着种子袋，坐在空椅上打瞌睡。

托马给你挪出普通的一张椅子。地图上有守望网的值岗点，也有尚未确认的工程支路。军队送来可以立即生效的指挥令，压在议事记录旁，末尾没有交权日期，送信人还在门口等着回执。

前置：d5_c_oath_4 / d5_c_revolt_3 / d5_h_revolt_2 / d5_h_guard_2 / d5_w_oath_4 / d5_w_revolt_3 / d5_w_guard_3 / d5_v_oath_1 / d5_v_ledger_3 / d5_v_revolt_2

### d6_v_oath_1 · 支持可撤回的共同承压协议，接受少数人离开。

当下理解：程序保留拒绝权，同时接受：力量并非最大。

实际后果：程序保留拒绝权；力量并非最大。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["shared_load"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_oath_2 · 把指挥交给受训者，自己守住会议后的道路。

当下理解：专业者得到空间，同时接受：你的名字可能不在公告里。

实际后果：专业者得到空间；你的名字可能不在公告里。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["yielded_command"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_oath_3 · 为种子与儿童保留第一批船位。

当下理解：灾后生活有了起点，同时接受：部分战斗物资被留下。

实际后果：灾后生活有了起点；部分战斗物资被留下。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["saved_seeds"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_oath_4 · 请求临时独裁到日落，用效率赌信任。

当下理解：命令迅速执行，同时接受：交权只剩你的承诺。

实际后果：命令迅速执行；交权只剩你的承诺。

下一节点：d7_c_oath；终局身份：None

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["emergency_dictator"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "下一日获得王令持有者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_v_ledger · 渡船的第七次往返

萨德在船板上刻完最后一条维修方法，用袖子擦去木屑。对岸王都的灯一片片灭下去，船工只看得到最近那盏靠岸灯。

浮桥缺木，伤者缺船位，两族水手已经来到渡口，却还各站在一边。萨德把自己的工具放进公用箱，船还能再走一趟。水涨到了昨天用来系绳的钉子。

前置：d5_c_ledger_2 / d5_h_guard_4 / d5_w_ledger_2 / d5_w_guard_1 / d5_v_oath_2 / d5_v_guard_1

### d6_v_ledger_1 · 保留渡船，把全局胜负交给上游工程。

当下理解：本地撤离可靠，同时接受：你无法亲自掌握大陆结局。

实际后果：本地撤离可靠；你无法亲自掌握大陆结局。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["kept_ferry"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_ledger_2 · 拆船作分流浮桥，把个人退路接成公共道路。

当下理解：更多人能步行撤离，同时接受：你失去机动撤退工具。

实际后果：更多人能步行撤离；你失去机动撤退工具。

下一节点：d7_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["made_public_bridge"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_ledger_3 · 把最后一班船留给伤员，自己划回暗处。

当下理解：没人独自等在岸边，同时接受：你要再次面对洪峰。

实际后果：没人独自等在岸边；你要再次面对洪峰。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"People": 1, "Companions": 1}, "add_flags": ["last_ferry_return"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_ledger_4 · 请两族水手共同守船，让家人先过河。

当下理解：家人与乘客获得照料，同时接受：船员必须克服旧怨。

实际后果：家人与乘客获得照料；船员必须克服旧怨。

下一节点：d7_h_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["mixed_ferry_crew"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得收容者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_v_revolt · 世界没有追上来

安全领重新开门，这次只要求放下武器。守卫把旧友名单收进柜子，递出居民登记纸；墙内有人正在分热水。

孩子先被领到檐下，屋外的流民仍在等接应。沿途记下的道路可以换到工程工具，也会让别人知道隐蔽的营地。门边的架子上还空着一个位置，恰好能放下你的行囊。

前置：d5_c_guard_3 / d5_v_revolt_1 / d5_v_guard_2

### d6_v_revolt_1 · 放下武器入城，替幸存者保存真实记忆。

当下理解：你能活着讲述，同时接受：这次不再返回战场。

实际后果：你能活着讲述；这次不再返回战场。

下一节点：d7_v_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["chose_exile"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得离群者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_revolt_2 · 请守卫接纳孩子，自己回去守最后的路。

当下理解：孩子进入城墙，同时接受：你放弃到手的安全。

实际后果：孩子进入城墙；你放弃到手的安全。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["returned_final_time"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_revolt_3 · 留在门外接应陌生人，不再加入任何军队。

当下理解：流民有了接应者，同时接受：你没有制度保护。

实际后果：流民有了接应者；你没有制度保护。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["independent_relief"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_revolt_4 · 用沿途记录换取工具，送往分压工地。

当下理解：工程得到物资，同时接受：安全领掌握各方隐秘道路。

实际后果：工程得到物资；安全领掌握各方隐秘道路。

下一节点：d7_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["traded_route_knowledge"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

## d6_v_guard · 你不必成为传说

撤离的人在临时灶边相聚，家人也赶到了这里。托马拿回一把修好的旧钥匙，放在桌上；如果房子已经不在，钥匙仍开得了留下的那只工具箱。

最后一碗汤正要分下去，船工来喊末班船。山闸传来缺人的消息，孩子们围着种子、病历和行李，等大人告诉他们该带走哪一件。锅底已经刮得发亮。

前置：d5_h_guard_3 / d5_w_guard_4 / d5_v_oath_3 / d5_v_ledger_1 / d5_v_revolt_3

### d6_v_guard_1 · 留在家与邻人之间，守好最后一盏灯。

当下理解：熟悉的人不再独处，同时接受：远处战局不受你控制。

实际后果：熟悉的人不再独处；远处战局不受你控制。

下一节点：d7_v_guard；终局身份：None

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"People": 1}, "add_flags": ["chose_home"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "下一日获得守家人的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_guard_2 · 把最后的船位留给家人，转身去守闸。

当下理解：家人有机会安全抵岸，同时接受：你放弃同行。

实际后果：家人有机会安全抵岸；你放弃同行。

下一节点：d7_c_guard；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 2}, "add_flags": ["final_rearguard"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得护送者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_guard_3 · 将种子、病历和钥匙分别交给三个孩子。

当下理解：未来不依赖一名幸存者，同时接受：你放弃独自保管遗产。

实际后果：未来不依赖一名幸存者；你放弃独自保管遗产。

下一节点：d7_v_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"People": 1}, "add_flags": ["distributed_future"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得渡口组织者的入口；行为永久保留在弧光与结局证据中。"}`

### d6_v_guard_4 · 拒绝任何封号，只以邻居身份参加共同承压。

当下理解：共同承担不需要英雄身份，同时接受：没有人许诺你会被记住。

实际后果：共同承担不需要英雄身份；没有人许诺你会被记住。

下一节点：d7_v_oath；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["refused_all_titles"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得民兵代表的入口；行为永久保留在弧光与结局证据中。"}`

## d7_c_oath · 印玺的日落

最后一轮命令堆在空着的摄政椅前，城门只剩一半还能升起。莱娅把王冠从软垫上拿开，露出下面用于宫墙护盾的接线。

维修队说，切开这一路能暂时保住中央撤离廊，也会先毁掉王宫。候选容器坐在另一边等交接，卫队等新口令，城外的队伍等开门。书吏把你的旧令也放进了同一个匣子。

前置：d6_c_oath_3 / d6_c_ledger_2 / d6_h_ledger_3 / d6_v_oath_4

### d7_c_oath_1 · 戴上王冠，将封印维护纳入公开国法。

当下理解：王国保留统一调度，同时接受：你必须接受长期问责。

实际后果：王国保留统一调度；你必须接受长期问责。

下一节点：None；终局身份：king

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "终局身份为国王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_oath_2 · 用王令组织自愿缓冲，亲自进入承压椅。

当下理解：旧容器得以休息，同时接受：你的身体成为新的封印。

实际后果：旧容器得以休息；你的身体成为新的封印。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_oath_3 · 撤掉宫墙护盾，先保住中央撤离走廊。

当下理解：致命峰值被导离人口核心，同时接受：王宫不可保全。

实际后果：致命峰值被导离人口核心；王宫不可保全。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_oath_4 · 交还御印，随最后一队难民走出城门。

当下理解：你的命令留下后果，同时接受：你以普通队员完成护送。

实际后果：你的命令留下后果；你以普通队员完成护送。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["refused_crown"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_c_ledger · 最后一笔预算

预算纸边烧焦了一角。维克把各区愿意接入的线路逐一标亮，奥伦在空栏写上复核者，再将无法保证的范围圈了出来。

若之前只完成局部准备，这里就只有局部指示灯亮。国库钥匙还在桌上，原账可以随撤离车带走，水闸则必须有人留下。最后一笔墨没干，铜管已开始震动，桌上的空杯也跟着移了一点。

前置：d6_c_ledger_1

### d7_c_ledger_1 · 按公开模型分流，保存所有失误记录。

当下理解：最大冲击被削弱，同时接受：受损街区仍需赔偿。

实际后果：最大冲击被削弱；受损街区仍需赔偿。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_ledger_2 · 把账目交给共同议会，自己留守水闸。

当下理解：本地安全得到维持，同时接受：你失去全局指挥。

实际后果：本地安全得到维持；你失去全局指挥。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["held_gate_final"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_ledger_3 · 接管国库与维修权，以统一预算重建王国。

当下理解：工程可以延续，同时接受：财政权集中到你手里。

实际后果：工程可以延续；财政权集中到你手里。

下一节点：None；终局身份：king

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "终局身份为国王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_ledger_4 · 保全原始账簿，带幸存者离开无法再守的城。

当下理解：真相得以传递，同时接受：城墙最终被放弃。

实际后果：真相得以传递；城墙最终被放弃。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_c_revolt · 刑台与议事桌

刑台没有拆，议事桌已经搬到旁边。造它们的是同一批木匠，剩下的木料刚好够补一段浮桥。

广场的人等你宣布结果，神谕终端又送来一份征用令。维修工守着封闭的核心，总开关仍封着，只能先停止广场这一处征用。卫队长问该保护证人还是清空道路，你面前还摆着那枚临时印玺，印泥盒的盖子被人留在一边。

前置：d6_c_revolt_2

### d7_c_revolt_1 · 把强制回路接到刑台，建立服从你的秩序。

当下理解：中央秩序恢复，同时接受：自由被写成需要许可的恩典。

实际后果：中央秩序恢复；自由被写成需要许可的恩典。

下一节点：None；终局身份：tyrant

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"People": -2, "Companions": -1}, "add_flags": ["enslaved_core"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "终局身份为暴君；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_revolt_2 · 拆掉刑台，把木料送去修撤离浮桥。

当下理解：惩罚被延后，同时接受：人群获得通行的道路。

实际后果：惩罚被延后；人群获得通行的道路。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["dismantled_scaffold"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_revolt_3 · 封住已经辨清的本地征用接口，把未知线路留给复核者。

当下理解：本地征用暂时停止，同时接受：总核心仍在运转，记录交给了复核者。

实际后果：本地征用暂时停止；总核心仍在运转，记录交给了复核者。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["isolated_local_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_revolt_4 · 接受公开选举的临时王位，立刻交出审判权。

当下理解：权力有了监督，同时接受：新制度仍可能失败。

实际后果：权力有了监督；新制度仍可能失败。

下一节点：None；终局身份：king

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为国王；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_c_guard · 路的尽头还有人

最后一队伤者停在山口。玛伦把盾靠在路边，替走不动的人重新绑好担架。前方能到新的边界，身后的黑潮正在越过废弃的岗楼。

这里没有城墙。守到所有人离开的人，将很难再追上队伍。玛伦把余下的绷带分开，一份挂在前行的车上，一份留在火盆旁。远处又有人喊，少了一辆车。

前置：d6_c_oath_4 / d6_c_revolt_4 / d6_c_guard_2 / d6_w_revolt_4 / d6_v_oath_2 / d6_v_revolt_2 / d6_v_guard_2

### d7_c_guard_1 · 带最后一队伤者穿过山口，然后放下武器。

当下理解：这一队人活着抵达，同时接受：你无法保证远处的城。

实际后果：这一队人活着抵达；你无法保证远处的城。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["escorted_last"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_guard_2 · 留下守住山口，让同行者全部先走。

当下理解：队伍脱离追来的黑潮，同时接受：你没有走出山口。

实际后果：队伍脱离追来的黑潮；你没有走出山口。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_guard_3 · 驻守新的边界，让这里永远接纳后来者。

当下理解：流民得到庇护，同时接受：守望将占据你此后的人生。

实际后果：流民得到庇护；守望将占据你此后的人生。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["founded_border_watch"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_guard_4 · 将指挥交给玛伦，独自寻找失联的村庄。

当下理解：你放弃稳定归宿，同时接受：无人照管的地方仍有人抵达。

实际后果：你放弃稳定归宿；无人照管的地方仍有人抵达。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为远行者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_h_oath · 祷词之后的回答

末次钟声落下，候选者仍坐在原位，等医师逐一确认。瑟文没有穿礼服，把权杖横放在两张普通椅子之间。

圣堂的供能可以改接撤离屏障，承压接口也已备好。工匠警告，前者会让祭坛先塌，后者需要一个仍清醒地答应的人。门外信徒收拾着行李，有人等仪式，有人只想等同行者出来。

前置：d6_c_oath_1 / d6_h_oath_1

### d7_h_oath_1 · 接下权杖，把拒绝与退出写成不可删改的教律。

当下理解：教会继续存在，同时接受：改革必须日复一日执行。

实际后果：教会继续存在；改革必须日复一日执行。

下一节点：None；终局身份：pontiff

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为教会领袖；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_oath_2 · 自愿接替旧容器，并让见证人定期复核同意。

当下理解：封印获得延续，同时接受：你承担漫长的痛苦。

实际后果：封印获得延续；你承担漫长的痛苦。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_oath_3 · 让圣堂供能转向撤离屏障，接受祭坛崩塌。

当下理解：人群越过危险峰值，同时接受：圣堂失去象征中心。

实际后果：人群越过危险峰值；圣堂失去象征中心。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_oath_4 · 拒绝就职，带着仍愿同行的人走出圣堂。

当下理解：信仰回到个人，同时接受：教会暂失统一领导。

实际后果：信仰回到个人；教会暂失统一领导。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["rejected_church"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_h_ledger · 不可删去的一页

原件与病历分装进两只箱子，录下的证词由第三个人带走。档案员试着合上箱盖，露出的那一页又被他仔细折回去。

核心维修图铺在地上，有来源可核对的接口才贴着封条。另一路能把记忆接入缓冲，医师说接入者未必还能完整回来。圣堂的灯还亮着，留下来接管它的人需要重新召集信徒。

前置：d6_c_revolt_1 / d6_h_oath_2 / d6_h_revolt_4

### d7_h_ledger_1 · 永久停用强制神谕核心，保存其计算档案。

当下理解：强制征用终止，同时接受：失去中央协调造成长期困难。

实际后果：强制征用终止；失去中央协调造成长期困难。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为弑神者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_ledger_2 · 成立独立记忆馆，陪证人离开封印城。

当下理解：篡改不再容易，同时接受：你没有亲自终结黑潮。

实际后果：篡改不再容易；你没有亲自终结黑潮。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_ledger_3 · 保留仪式，接管教会并开放所有原始档案。

当下理解：信徒仍有共同组织，同时接受：公开真相引发分裂。

实际后果：信徒仍有共同组织；公开真相引发分裂。

下一节点：None；终局身份：pontiff

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为教会领袖；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_ledger_4 · 把自己的记忆接入缓冲层，为维修队争到时间。

当下理解：维修得以完成一轮，同时接受：你的人格不能完整回来。

实际后果：维修得以完成一轮；你的人格不能完整回来。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_h_revolt · 魔王最后的名字

艾德里安请你念一次他的名字，确认窗边的人听清了。他的停止请求夹在病历最上面，银管里的压力没有因此下降。

医师清点可用缓冲，工匠核对神谕接口。未经验证的管路被绑了红绳，不能直接接入。门外病人开始撤离，瓦尔的旗已卷起来。艾德里安把药杯递给你，杯底只剩一点水。

前置：d6_c_guard_1 / d6_h_oath_3 / d6_h_ledger_1

### d7_h_revolt_1 · 接替艾德里安，公开承认魔王是一份职责。

当下理解：旧勇者得以休息，同时接受：偏见不会随公告消失。

实际后果：旧勇者得以休息；偏见不会随公告消失。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_revolt_2 · 断开强制神谕，与两族共同维护余下的封印。

当下理解：奴役接口被关闭，同时接受：维护成本由社会承担。

实际后果：奴役接口被关闭；维护成本由社会承担。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_revolt_3 · 尊重他的停止请求，将余压导入预留缓冲。

当下理解：艾德里安平静死去，同时接受：缓冲为居民争到存续时间。

实际后果：艾德里安平静死去；缓冲为居民争到存续时间。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["released_previous_hero"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_revolt_4 · 带走他的证词，护送病房里的平民离城。

当下理解：历史有了幸存证人，同时接受：封印由留下的人接手。

实际后果：历史有了幸存证人；封印由留下的人接手。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_h_guard · 病房门外的黎明

伊芙洗净最后一双手套，把一张病床推到门槛前。床轮卡住，她退后一点，换个角度又推了一次。

船工在外面清点床号，中立医院的契约等人续签。留下维持重症屏障的人要等到灯尽，医师不敢答应还有回程。一个已经能走的病人来帮忙抬床脚，问钥匙最后该交给谁。

前置：d6_c_revolt_3 / d6_h_revolt_2 / d6_h_guard_1 / d6_w_revolt_3 / d6_v_ledger_4

### d7_h_guard_1 · 接下医院的终身守护契约，拒绝军事征用。

当下理解：伤者有了中立家园，同时接受：守护并不等于没有敌人。

实际后果：伤者有了中立家园；守护并不等于没有敌人。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["protected_hospital"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_guard_2 · 把病床编成船队，亲自带到安全岸。

当下理解：病人跨过黑潮支流，同时接受：物资只能留在原处。

实际后果：病人跨过黑潮支流；物资只能留在原处。

下一节点：None；终局身份：ferryman

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["ferried_beds"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为摆渡人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_guard_3 · 留在最后一盏灯下，以生命维持重症屏障。

当下理解：重症者等到撤离，同时接受：你在灯熄后死去。

实际后果：重症者等到撤离；你在灯熄后死去。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_guard_4 · 拒绝任何职务，回村照料幸存的邻人。

当下理解：你保有一段普通生活，同时接受：世界的修复不会因此完成。

实际后果：你保有一段普通生活；世界的修复不会因此完成。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为普通人；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_w_oath · 椅子不是王座

承压椅的扶手裂了一道口，工匠用布缠住木刺。古龙让所有人后退半步，给还没签名的人留出起身的位置。

外环需要人挡住第一轮黑潮，分流需要核过方向的管道；不齐全的记录仍压在桌上。门口也能改成轮值哨所，存下来的工具够用。椅上没人催促，墙里的水声却越来越响。

前置：d6_c_ledger_3 / d6_h_oath_4 / d6_h_ledger_4 / d6_h_revolt_1 / d6_w_oath_1 / d6_w_ledger_2 / d6_w_guard_4

### d7_w_oath_1 · 坐进承压椅，接下有期限的魔王职责。

当下理解：大陆获得下一段时间，同时接受：继任问题没有消失。

实际后果：大陆获得下一段时间；继任问题没有消失。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_oath_2 · 站在外环承担第一轮黑潮，掩护所有值守者退后。

当下理解：维护者保存下来，同时接受：你的生命耗尽。

实际后果：维护者保存下来；你的生命耗尽。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_oath_3 · 以承压训练稳定峰值，再把维护交给共同守望队。

当下理解：最危险的一轮过去，同时接受：长期维护仍需要众人。

实际后果：最危险的一轮过去；长期维护仍需要众人。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_oath_4 · 将封印外门改成共同哨所，与龙族轮值。

当下理解：守门职责不再独占，同时接受：休息必须以他人的接班换来。

实际后果：守门职责不再独占；休息必须以他人的接班换来。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["shared_watch_final"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_w_ledger · 图纸外的一毫米

最后一枚接头偏了一毫米。缇尔将误差写在铜片上，工匠因此多绕了一段线；未经验证的支路仍贴着禁止启动的红纸。

空域方向的灯等待确认，核心接口上另有一道权限锁。你带来的记录决定哪些开关可以动。维修队开始往外送图纸，最年轻的学徒抱不动整箱，只能先带走一半。

前置：d6_c_oath_2 / d6_h_ledger_2 / d6_w_oath_2 / d6_v_revolt_4

### d7_w_ledger_1 · 启动经现场复核的分流，把灾难峰值引向空域。

当下理解：大陆避过即时崩塌，同时接受：污染与维修债留给生者。

实际后果：大陆避过即时崩塌；污染与维修债留给生者。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_ledger_2 · 拆除强制分配中枢，让接口从此只能自愿接入。

当下理解：旧神谕的权力终止，同时接受：新秩序需要重新协商。

实际后果：旧神谕的权力终止；新秩序需要重新协商。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_ledger_3 · 把最后的过载引进自己，保住维修人员。

当下理解：图纸有人继续执行，同时接受：你不能看见完成的系统。

实际后果：图纸有人继续执行；你不能看见完成的系统。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_ledger_4 · 保存开源图纸，踏上寻找失联节点的道路。

当下理解：知识随你流动，同时接受：你失去安稳归宿。

实际后果：知识随你流动；你失去安稳归宿。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为远行者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_w_revolt · 没有人能命令你

核心将整座城的阀门送到控制台上。街上的人抬头时，表针便升起一点；只要持续抽取他们的恐惧，屏障还能维持。

旁边留着一个活体接口，撤离通道也尚未封死。工匠把控制器放在你够得到的地方，随后退到门外。仪表的上限涂着红漆，指针已经碰到边缘，还在向前。

前置：d6_w_ledger_4 / d6_w_revolt_2

### d7_w_revolt_1 · 独占核心，以恐惧维持一座不会反抗的城。

当下理解：城内暂时安定，同时接受：居民的意志成为燃料。

实际后果：城内暂时安定；居民的意志成为燃料。

下一节点：None；终局身份：tyrant

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"People": -2, "Companions": -1}, "add_flags": ["enslaved_core"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "终局身份为暴君；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_revolt_2 · 把力量封入自己的身体，停止向他人索取。

当下理解：黑潮有了新容器，同时接受：你无法轻易走出封印。

实际后果：黑潮有了新容器；你无法轻易走出封印。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_revolt_3 · 用残余力量撕开撤离通道，然后交出控制器。

当下理解：人群得救，同时接受：你必须面对此前的伤害。

实际后果：人群得救；你必须面对此前的伤害。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["surrendered_power_final"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_revolt_4 · 拒绝任何限制，向黑潮索取超过身体的力量。

当下理解：力量越过容器极限，同时接受：附近的屏障随你一起破裂。

实际后果：力量越过容器极限；附近的屏障随你一起破裂。

下一节点：None；终局身份：failed

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {}, "add_flags": ["lost_self"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "终局身份为失控者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_w_guard · 鳞片与炊烟

幼龙的呼吸平稳下来，难民营第一次升起做饭的烟。阿瑟兰把修好的食槽推到门口，等被火伤过的村民来决定还用不用。

巢外的护盾缺了一角，照护名册也还空着几个班次。去新栖地的车已经套好，公开的承压契约摆在炉边。一个孩子摸了摸幼龙的鼻子，随即回头找大人的手。

前置：d6_w_oath_3 / d6_w_revolt_1 / d6_w_guard_1

### d7_w_guard_1 · 成为两族照护人的一员，守护龙巢与周边村庄。

当下理解：共居开始，同时接受：双方仍需面对旧伤。

实际后果：共居开始；双方仍需面对旧伤。

下一节点：None；终局身份：dragonkeeper

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Dragons": 2}, "add_flags": ["kept_dragon_care"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为养龙人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_guard_2 · 把龙巢护盾留给病人，自己守住破损外墙。

当下理解：弱者获得保护，同时接受：你把余生留在边界。

实际后果：弱者获得保护；你把余生留在边界。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["held_gate_final"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_guard_3 · 与龙族签公开轮值约，接下第一期容器职责。

当下理解：封印延续，同时接受：龙族不能再置身事外。

实际后果：封印延续；龙族不能再置身事外。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_guard_4 · 放下看守权，护送幼龙与孩子去新的栖地。

当下理解：孩子不再继承旧战场，同时接受：你也告别熟悉的家。

实际后果：孩子不再继承旧战场；你也告别熟悉的家。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为远行者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_v_oath · 你的椅子也是木头

议事桌旁添了一把普通木椅，没有放高。承压表和守桥表并排传阅，未验证的工程部分仍被划在红线外。

有人带来限期执政的印玺，日期还要刻上去。有人只想归还徽记，回去补屋顶。桥上的队伍正在移动，孩子抱着种子袋让开门口，给下一个进来签名的人留了位置。

前置：d6_c_guard_3 / d6_h_guard_4 / d6_w_oath_4 / d6_w_ledger_3 / d6_v_ledger_2 / d6_v_guard_4

### d7_v_oath_1 · 签下共同维护协议，亲自参加第一轮承压。

当下理解：灾难峰值得到分担，同时接受：人人仍有长期责任。

实际后果：灾难峰值得到分担；人人仍有长期责任。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["collective_final"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_oath_2 · 归还代表徽记，以邻居身份开始重建。

当下理解：你回到日常，同时接受：制度由其他代表继续维护。

实际后果：你回到日常；制度由其他代表继续维护。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为普通人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_oath_3 · 接受限期执政职位，把交权日期刻在印玺上。

当下理解：调度得到延续，同时接受：日期能否兑现仍需监督。

实际后果：调度得到延续；日期能否兑现仍需监督。

下一节点：None；终局身份：king

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为国王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_oath_4 · 拒绝王位，带民兵守到最后一名撤离者过桥。

当下理解：桥上无人被独留，同时接受：你付出伤病与时间。

实际后果：桥上无人被独留；你付出伤病与时间。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["escorted_last"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_v_ledger · 让明天不再需要一个人

渡口收到上游信号，工匠摊开试验单和居民签名。两样都齐的支路才亮灯，缺证的地方仍用木闸维持，不能靠一句同意接上去。

末班船贴着岸，水路图已经装入防水筒。闸底的手轮必须有人压住，水越涨，松手的余地越小。船工没有催你，先替还没上船的人扶稳了踏板。

前置：d6_c_guard_4 / d6_h_guard_2 / d6_w_ledger_1 / d6_w_guard_2 / d6_v_oath_1 / d6_v_ledger_1 / d6_v_guard_3

### d7_v_ledger_1 · 接通自愿分压网络，把开关留在每个居民手中。

当下理解：按前置验证决定长期转型或短期稳压，同时接受：生活将失去旧文明的便利。

实际后果：按前置验证决定长期转型或短期稳压；生活将失去旧文明的便利。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["collective_final"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_ledger_2 · 不冒险扩大系统，完成最后一轮渡运。

当下理解：岸边的人得救，同时接受：大陆封印由别处继续维护。

实际后果：岸边的人得救；大陆封印由别处继续维护。

下一节点：None；终局身份：ferryman

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["ferried_last"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为摆渡人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_ledger_3 · 把船位让给同伴，自己留在闸底扳住手轮。

当下理解：同伴得以离开，同时接受：水压最终夺去你的生命。

实际后果：同伴得以离开；水压最终夺去你的生命。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_ledger_4 · 保存水路与维修图，带证人去安全领。

当下理解：下一次灾难不必从零开始，同时接受：你离开故乡。

实际后果：下一次灾难不必从零开始；你离开故乡。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_v_revolt · 门在你身后关上

安全领的登记桌上摆着一盏灯。书吏问明天想做什么，只需填一个职业，不必补上勇者或逃兵。

你带来的记录有几处空白，正是当时离开而没能看见的地方。出城门仍开着，能去更远的无名村庄。书吏将一把普通钥匙推过来，笔尖蘸好了墨，等你的第一行字。登记桌旁已经排来了下一家人。

前置：d6_v_revolt_1

### d7_v_revolt_1 · 登记为居民，认真活完这段被争取来的日常。

当下理解：你开始新生活，同时接受：离开的人仍可能责怪你。

实际后果：你开始新生活；离开的人仍可能责怪你。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为普通人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_revolt_2 · 承认离开战场，拒绝接受任何追授的荣耀。

当下理解：身份诚实，同时接受：你失去方便的英雄叙事。

实际后果：身份诚实；你失去方便的英雄叙事。

下一节点：None；终局身份：exile

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["accepted_exile"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为流亡者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_revolt_3 · 写下所有见闻，包括自己没能回去的那一天。

当下理解：记录留下缺口与羞耻，同时接受：真相不再只由赢家书写。

实际后果：记录留下缺口与羞耻；真相不再只由赢家书写。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_revolt_4 · 离开安全领，去那些没有出现在地图上的地方。

当下理解：你再次承担未知，同时接受：没有人许诺你的回归。

实际后果：你再次承担未知；没有人许诺你的回归。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为远行者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_v_guard · 第七碗汤

远处的光没能照清是谁的旗。邻人送来种子，孩子用布塞住门缝，一锅汤煮开后，屋里终于不再只听见外堤的水声。

渡船靠岸送来两族留下的孩子，同行的照护人问村里能否再添几个床位。河边还有人未过岸，外堤也还缺守夜者。托马数完碗，把最后一只洗净，放在灶台边。屋外的脚步在门槛前停了下来。

前置：d6_c_ledger_4 / d6_h_revolt_3 / d6_h_guard_3 / d6_w_guard_3 / d6_v_oath_3 / d6_v_ledger_3 / d6_v_revolt_3 / d6_v_guard_1

### d7_v_guard_1 · 留在故乡，照顾活下来的人并承认自己的限度。

当下理解：日常重新开始，同时接受：失去的人不会因此回来。

实际后果：日常重新开始；失去的人不会因此回来。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为普通人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_guard_2 · 沿河撑船，把汤和药送给还未过岸的人。

当下理解：河岸得到接应，同时接受：你再次离开家门。

实际后果：河岸得到接应；你再次离开家门。

下一节点：None；终局身份：ferryman

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["ferried_last"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为摆渡人；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_guard_3 · 守在外堤，让村里的人安睡第一夜。

当下理解：故乡得到缓冲，同时接受：你的守望还未结束。

实际后果：故乡得到缓冲；你的守望还未结束。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["held_gate_final"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_v_guard_4 · 将龙族与人类留下的孩子一起养大。

当下理解：新一代有了共同的家，同时接受：旧社会未必欢迎它。

实际后果：新一代有了共同的家；旧社会未必欢迎它。

下一节点：None；终局身份：dragonkeeper

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Dragons": 2}, "add_flags": ["kept_dragon_care"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为养龙人；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_w_oath_sword · 黎明的四种用途

黎明仍握在你手里。工匠量过剑身，够做导流针，也能切断已辨清的征用接口；不明的接线还封着，剑光照不出它们通往哪里。

门外两族伤者认得这柄剑，追兵也认得。古龙将一次性屏障的接法画在地上，剑若折断，守缺口的人便没有第二次机会。所有人退开，给你的手留出地方。

前置：d6_c_ledger_3 / d6_h_oath_4 / d6_h_ledger_4 / d6_h_revolt_1 / d6_w_oath_1 / d6_w_ledger_2 / d6_w_guard_4

### d7_w_oath_sword_1 · 将黎明化为导流针，自愿接替旧容器。

当下理解：圣剑进入封印而非王座，同时接受：你的生命成为承压边界。

实际后果：圣剑进入封印而非王座；你的生命成为承压边界。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_oath_sword_2 · 用黎明切断神谕征用接口，保留人工维护回路。

当下理解：强制征用被终止，同时接受：圣剑永久失去完整剑身。

实际后果：强制征用被终止；圣剑永久失去完整剑身。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_oath_sword_3 · 将黎明举作停火信号，护送两族伤者离开。

当下理解：威望被用来停止追杀，同时接受：你放弃亲自统治核心。

实际后果：威望被用来停止追杀；你放弃亲自统治核心。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["sword_as_signal"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_oath_sword_4 · 折断黎明释放一次屏障，自己守住崩裂缺口。

当下理解：众人得到撤离窗口，同时接受：你与圣剑一同留在缺口。

实际后果：众人得到撤离窗口；你与圣剑一同留在缺口。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为殉道者；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_w_guard_dragon_debt · 没有古龙签名的契约

遗誓使带来阿瑟兰的遗骨，把它放在你的工具旁。赔偿名单写着守境、离境和公开证词，没有哪一栏要求受害者原谅。

幼龙已经交给共同照护人，不再由你单独决定去处。封印少了古龙的一个支点，容器接口仍可接上。门外有人受过你的帮助，也有人一眼认出了骨头上的伤口。

前置：d6_w_oath_3 / d6_w_revolt_1 / d6_w_guard_1

### d7_w_guard_dragon_debt_1 · 接受监督，守住受损龙境并长期偿还赔偿。

当下理解：边界得到保护，同时接受：你不再拥有自由离开的权利。

实际后果：边界得到保护；你不再拥有自由离开的权利。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["accepted_dragon_reparation"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_guard_dragon_debt_2 · 交出全部屠龙记录，让两族分别保存证词。

当下理解：死亡不会被功绩隐去，同时接受：你接受公开审查。

实际后果：死亡不会被功绩隐去；你接受公开审查。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_guard_dragon_debt_3 · 把幼龙交给共同照护会，接受永久离境。

当下理解：幼龙不必由杀死父亲的人监护，同时接受：你失去归处。

实际后果：幼龙不必由杀死父亲的人监护；你失去归处。

下一节点：None；终局身份：exile

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["accepted_exile"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为流亡者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_w_guard_dragon_debt_4 · 以新的容器职责补上失去的承压支点。

当下理解：灾难得到一次缓冲，同时接受：这不是对屠龙的自动赦免。

实际后果：灾难得到一次缓冲；这不是对屠龙的自动赦免。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_c_oath_judgment · 加冕之前，先读出名单

长桌上没有铺加冕的绒布，受害者把名单一张张摆开。莱娅让卫队退到门边，证人自行念出姓名和收到过的命令。

印玺还在你手里，城里的调度也仍需要人接管。独立审判的条款只差最后一枚印，另一队卫兵则等你下令清场。有人念到一半停住了，身旁的人接过那张纸。

前置：d6_c_oath_3 / d6_c_ledger_2 / d6_h_ledger_3 / d6_v_oath_4

### d7_c_oath_judgment_1 · 接受有独立审判监督的王位，公开承担旧令责任。

当下理解：王国保有调度，同时接受：你的罪责不受王位豁免。

实际后果：王国保有调度；你的罪责不受王位豁免。

下一节点：None；终局身份：king

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为国王；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_oath_judgment_2 · 交出印玺，先完成受害者要求的撤离任务。

当下理解：一批人获得救援，同时接受：你不能据此要求撤回控诉。

实际后果：一批人获得救援；你不能据此要求撤回控诉。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["submitted_to_victims"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_oath_judgment_3 · 签下自己的供词，把证据送出王都。

当下理解：证据不再受你控制，同时接受：王位可能由对手取得。

实际后果：证据不再受你控制；王位可能由对手取得。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_c_oath_judgment_4 · 让卫队驱逐证人，以封印危机为由永不交权。

当下理解：你的命令不再被打断，同时接受：受害者失去拒绝的权利。

实际后果：你的命令不再被打断；受害者失去拒绝的权利。

下一节点：None；终局身份：tyrant

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"People": -2, "Companions": -1}, "add_flags": ["enslaved_core"], "remove_flags": [], "arc_tags": ["ambition", "harm"], "long_term": "终局身份为暴君；条件不齐时执行 fallback，罪责仍保留。"}`

## d7_h_oath_dissent · 曾经离开的人回来了

你再次跨进圣堂。枢机递来撤回异议的声明，信徒却把你当时提出的问题放在声明上，纸边早已磨软。

权杖、病历和神谕维修图都在桌上。维修记录不足以关闭总核心。已辨清的本堂接口可以停用，其余接线仍保持封闭。瑟文搬来一把椅子，没有问你是否终于认错，只问今晚愿意留下做什么。

前置：d6_c_oath_1 / d6_h_oath_1

### d7_h_oath_dissent_1 · 以异议者身份接任，确立任何人都能退出的教律。

当下理解：信仰与质询暂时共处，同时接受：顽固派拒绝承认你。

实际后果：信仰与质询暂时共处；顽固派拒绝承认你。

下一节点：None；终局身份：pontiff

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为教会领袖；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_oath_dissent_2 · 封住已经辨清的本地征用接口，把未知线路留给复核者。

当下理解：本地征用暂时停止，同时接受：总核心仍在运转，记录交给了复核者。

实际后果：本地征用暂时停止；总核心仍在运转，记录交给了复核者。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["isolated_local_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为勇者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_oath_dissent_3 · 拒绝权杖，保存教会的功绩与罪行原件。

当下理解：历史不再只有颂歌或控诉，同时接受：你失去改革的职位。

实际后果：历史不再只有颂歌或控诉；你失去改革的职位。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为见证者；条件不齐时执行 fallback，罪责仍保留。"}`

### d7_h_oath_dissent_4 · 不向教会效忠，只以个人身份接受容器交接。

当下理解：封印得到延续，同时接受：你的同意不属于任何神职者。

实际后果：封印得到延续；你的同意不属于任何神职者。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；条件不齐时执行 fallback，罪责仍保留。"}`