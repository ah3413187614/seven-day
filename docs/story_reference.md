# 七日全节点策划（DESIGNER_ONLY）

## d1_start · 第七声钟响之前

召集令钉在故乡的门上，雨水把“勇者”两个字浸得发黑。七天后，魔王的封印将崩塌。王国承诺土地、金钱与史书中的名字，教会承诺祝福。托马没有承诺任何东西，只把一箱修桥的工具放在门边。你还没有被谁选中，也不知道召集令背后隐藏着什么。天亮以后，你只能赶往一个地方。

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

阿尔维恩的城门只向四类人开启：能作战的、能付钱的、能证明有用的，以及有人担保的。骑士玛伦替你作保，却把你的粮单压在一摞阵亡通知之下。摄政莱娅答应派粮，但她需要一个在广场上接受勇者封号的人。账房的墨还没有干，名单里已有三座被放弃的村庄。城外的队伍等不到下一次议事。

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

钟声响了六次，第七声迟迟没有来。修女伊芙说那口钟只在封印稳定时鸣响；执事却坚持只是钟轴生锈。你带来的预言抄本少了一页，装订线里夹着七百年前的血。院外有人要烧死一名带角的信使，院内有人在为人类伤兵缝合伤口。他们唱的是同一首圣歌，教皇瑟文正在两扇门之间等你的回答。

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

精灵旧林的路牌全部朝向来处。地图师缇尔说，林子不是在驱逐你，而是在给你最后一次离开的机会。断裂的祭坛上没有宝石，只有一柄被布条包住的剑。它没有审问你的善恶，只让你看见自己死去的样子。更深处传来龙卵敲壳的声音，山下猎人已经点起熔炉。你来寻找力量，力量却先提出了要保护什么的问题。

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

河水把桥墩磨成了骨头的颜色。父亲留下的工具仍在门边，村长托马没有问你为什么没去当勇者，只问明早能过几辆车。驻军要拆桥阻止魔族斥候，船工要留桥转移病人。妮娅送来上游决堤的消息，没有人愿意相信一个魔族孩子。你留下以后，故乡没有变得简单：至少有三种死亡正在沿着不同的路接近。

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

你的王令能让粮仓开门，也能让士兵征走最后一匹马。玛伦请你在军需单上签字，单子背面却粘着一张平民的求救信。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

消失的军粮并不全在贵族地窖里。账房奥伦用假账养着一座未被王国承认的麻风村；同一条运输线也在出售军情。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

你的发言让民众聚集，也让城门成为弓弩的靶场。莱娅承诺会谈，但要求你交出最先敲钟的工匠。工匠说自己愿意坐牢，却不肯认罪。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

难民车队抓到一名魔族少年，背包里装着绘有防线的地图。妮娅认出那是她哥哥的笔迹：地图同时标着一处将被洪水淹没的营地。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

你获准进入钟楼。仪表记录的不是魔力，而是某个人七百年的心跳。瑟文请你把那个人仍然活着的事实写成神迹。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

七位不同时代的勇者留下相同的伤口图。伊芙说，她救过一名魔族士兵，伤口里也有同样的黑砂。有人在外面索要这些病历作为异端罪证。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

妮娅的证词能证明魔族平民正在撤离，却也会暴露一条秘密山道。魔族将领瓦尔请求你删去山道位置；他不愿说这条路还会运输什么。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

最后一瓶止血药放在伊芙掌心。左床的人类军官掌握撤离口令，右床的魔族工兵知道封印排水渠。两人都清醒，也都听见了你们的讨论。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

黎明在你掌中发热，却没有阻止猎人殴打盗粮者。缇尔提醒你，剑回应的是肯付出的意志，而不是善恶。猎人也愿意为饿着的女儿去死。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

古代管道从教堂、王宫和龙巢同时流向山腹。缇尔发现系统仍在工作，维修铭文却被凿掉。开启检修门需要停止一处供能。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

当下理解：获得可靠波形，同时接受：全城看见圣灯熄灭。

实际后果：获得可靠波形；全城看见圣灯熄灭。

下一节点：d4_h_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Church": 1}, "add_flags": ["measured_abyss"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得禁书读者的入口；行为永久保留在弧光与结局证据中。"}`

### d3_w_ledger_4 · 用自己的生命火种启动旧机器。

当下理解：不用切断任何街区，同时接受：你开始咳血。

实际后果：不用切断任何街区；你开始咳血。

下一节点：d4_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["life_powered_machine"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d3_w_revolt · 被夺走的冬天

熔炉芯能破开龙鳞，也能让山镇度过寒冬。猎人头领追到断桥，没有要求你归还一切，只要你保证他的女儿不会冻死。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

古龙阿瑟兰没有为你护卵道谢。它问，如果龙的孩子需要烧毁一片村庄才能活，你是否仍会保护它。缇尔说，龙的誓言通常从这种问题开始。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

民兵在谷口发现两支队伍：王国溃兵带着伤者，魔族侦察兵带着水源图。桥只能容一支先过，另一支必须面对涨水。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

渡船的重量上限比乘客名单少三个人。托马把自己的名字划掉，另两名老人却不愿替任何人作榜样。妮娅带来一条穿过禁林的小径。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

你已经能看见安全领的烽火。身后传来桥钟，它本该在所有人过河后敲响，现在却提前了三个时辰。家人紧握你的袖口，没有要求你回头。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

老人把炉边的位置让给一个魔族伤兵。伤兵是工兵萨德，承认他曾炸毁王国的桥，也承认自己的部队不会回来接他。外面的巡逻队要你交人。第三日，新的道路已经打开，旧日的承诺却没有自动解除。昨天获得的许可、工具或同行者让你进入这里，也把一份需要兑现的责任带了进来。日落前只能完成一项行动，其他事情将由留下的人继续处理。

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

莱娅交出一份只有摄政才能看的继任诏书。每一位勇者名字后面，都留着一个尚未填写的死亡日期。她的父亲拒绝过选拔，代价是北岸三万人死于黑潮。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Kingdom": 1}, "add_flags": ["learned_truth"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得账簿调查者的入口；行为永久保留在弧光与结局证据中。"}`

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

账簿中七百年前的庆功宴之后，是向魔王城持续七百年的药材供给。奥伦把运单与现任封印心跳对齐：被运送的不是毒药，而是止痛药。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

你公开的证据被印成传单，最末一行却被改成“杀尽教士”。工匠维克承认印坊已失去控制。广场另一端，几个教士正在为踩踏伤者包扎。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

伤员玛伦认出封印画像中的人：不是被杀死的魔王，而是史书里的第一代勇者艾德里安。她问你是否还要把这批伤员送去参加所谓讨伐。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

瑟文带你见到钟楼下的传声管。所谓女神答复，有些来自祭司，有些来自旧机器，还有些连教皇也无法解释。他愿以自己的命证明维持封印不是骗局。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

当下理解：来源可以交叉核验，同时接受：各方争抢解释权。

实际后果：来源可以交叉核验；各方争抢解释权。

下一节点：d5_w_ledger；终局身份：None

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["studied_oracle"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "下一日获得遗迹测绘者的入口；行为永久保留在弧光与结局证据中。"}`

### d4_h_oath_4 · 接替教皇承受一次回流，确认他是否说谎。

当下理解：你证实回流真实，同时接受：体内黑纹扩散。

实际后果：你证实回流真实；体内黑纹扩散。

下一节点：d5_w_oath；终局身份：None

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Dragons": 1, "Companions": 1}, "add_flags": ["tested_burden"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "下一日获得契约者的入口；行为永久保留在弧光与结局证据中。"}`

## d4_h_ledger · 七百年的同一个人

删去的最后一页写着第一代勇者的亲笔请求：“若有人还能承受，就不要再称他为怪物。”伊芙发现王国与魔族都在删改这句话，各自只保留对自己有利的半句。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

前置：d3_c_oath_2 / d3_c_ledger_2 / d3_h_oath_2 / d3_w_ledger_3

### d4_h_ledger_1 · 公布完整原件，连同各方删改痕迹。

当下理解：任何阵营都难独占解释，同时接受：脆弱停火面临考验。

实际后果：任何阵营都难独占解释；脆弱停火面临考验。

下一节点：d5_c_revolt；终局身份：None

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"People": 1}, "add_flags": ["learned_truth"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "下一日获得抗命者的入口；行为永久保留在弧光与结局证据中。"}`

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

艾德里安坐在一把维修椅上，背后是穿过骨骼的银管。他知道历代勇者的名字，因为每一个都曾来这里问过是否还有别的办法。瓦尔在门外要求他给战争背书。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

伤者听见真相后没有立刻互相原谅。人类军官仍记得萨德炸断的桥，萨德也记得教会焚毁的村。伊芙把两人的床隔开，说止痛不能代替审判。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

古龙说黎明曾在艾德里安手中，也曾回应准备屠城的继任者。它认得愿付生命的信念，无法判断信念是否值得。剑柄的热度只是你自己的决心。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

缇尔发现所谓古龙墓地是深渊泄压系统。龙族守护墓地，也垄断了维修知识；七百年前它们同意单一容器方案，是为了不让自己的族群长期承压。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

炉芯与黑潮发生共鸣。瓦尔愿用一份屠龙图换你替他打开人类边防；阿瑟兰则愿烧毁一个魔族营地，换你交还炉芯。两份交易都把平民写成了空地。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

幼龙第一次喷火，烧伤了替它准备食物的村民。阿瑟兰愿赔偿，却要求任何人不得记录伤者姓名，以免龙族受辱。幼龙蜷在你的衣角里。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

托马找到旧村志：第一代勇者出发时，也只是负责修渠的年轻人。召集令之外，还有许多人维持了封印。民兵却开始要求你像王一样决定谁能留下。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

王都提供的撤离图没有你的故乡，也没有魔族河岸聚落。空白处恰好是泄压系统的旧出口。工匠维克说，修复它能救王都，却可能淹没这些房屋。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

安全领只接收与战争无关的人。守卫说你若交出全部证词、炉灰和旧友名单，就可以重新做个普通人。墙内灯火平稳，墙外钟声仍然断断续续。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

失控的记忆从地下传来。你看见艾德里安最后一次回家时，也站在这样一扇修不好的门前。托马说听见真相不等于承担全部责任，但现在已经不能假装没听见。第四日，封印的衰弱已无法靠传言遮掩。不同阵营带来的原件指向同一件事：被称为魔王的生命仍在压制深渊。知道真相不能取消眼前的危险，只使每一种行动都多了一层必须承担的后果。

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

### d4_v_guard_3 · 循记忆找到旧渠，亲自去见艾德里安。

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

莱娅愿给你战时摄政权，条件是继续容器制度。她没有否认制度残酷，只问没有替代方案时谁来承担溃坝。玛伦在桌上放了一封尚未签名的辞职信。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

维克的分压模型显示，保住中央城区最稳妥的方法是关闭外环三处闸门。奥伦提醒你，那里不是三个点，而是三个仍住着人的街区。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

维克得到粮仓，随后发现开门之后还要分粮。最先支持你的人要求双份；守仓的旧官员熟悉配给，却曾经殴打饥民。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

玛伦承认曾奉命烧毁一处魔族哨站，事后才知道地下藏着平民。瓦尔要求交出她作为停火条件。她不求你赦免，只求你不要把她的罪说成误会。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

瑟文辞去教皇之位，以便作为普通志愿者进入容器候选名单。枢机要求你接过权杖，或者让一名主张强制选拔的主教继任。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

研究已证实深渊是旧文明把痛苦从城市抽走后形成的回流海。所谓女神“曙母”曾是保护人的分配意志，后来把稳定凌驾于个人同意。机器中仍有无法归类的回应。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

瓦尔同意让平民撤离，却要把和平写成自己的胜利。妮娅说若签字，失去家人的魔族会再次被军队代表；若不签，今夜就没有通行保证。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

医院门口排起要求伊芙裁判战争的长队。她说可以确认谁受了伤，却不能仅凭伤口决定谁拥有土地。病床的数量已经不足以承载所有人的愤怒。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

阿瑟兰教你承压，第一条却是不要把愿意牺牲误当作必须牺牲。艾德里安请求你允许他停止。停止意味着必须立刻找到替代承压者或打开分流。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

缇尔的图纸能把深渊回流接回日常生活，代价是大陆不再享有旧文明提供的无痛与恒温。研究中没有全胜，只存在比永久容器更可分担的痛苦。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

你的力量使军队退开，也使朋友不敢靠近。深渊许诺可以替你承担犹豫，只要你允许它把别人的恐惧当作燃料。那声音并不吼叫，它非常体贴。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

阿瑟兰愿加入分压，但要求你先保证幼龙绝不承担风险。村里的孩子没有同样的保证。古龙沉默了很久，说它也知道这句话不公平。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

议事会选你作代表，却没有授予你替全体赴死的权利。有人愿参加分压，有人只想离开。托马说，共同生活不能要求每个人都当勇者。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

渡口还有一次往返时间。一边是分压工程所需的铜线，一边是尚未撤走的住户。萨德说可以徒手修闸，但有可能再也握不住任何东西。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

城外营地没有官员，也没有统一的粮仓。一个家庭拒绝共享食物，却在夜里向你借药。你能坚持自由，也能看见自由无法自动煮出晚饭。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

家人希望你留在身边，托马希望你帮助全村。两个请求都不卑鄙。黑潮没有等你处理完这些关系，水井里已经出现星光般的黑砂。第五日，封印的间歇越来越短。已经失去的东西不会因为改换立场而归还，愿意继续同行的人也各有底线。今天作出的安排，将决定明晚你能获得怎样的支援，以及谁会为此付出代价。

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

战时印玺已经能命令军队，不能命令封印不再破裂。莱娅把自己的名字写入承压名单，表示摄政家族没有豁免。将军们要你在秩序、继任与撤离之间先保住一项。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

维克在最后一版模型上写下失误范围，没有把它藏进脚注。奥伦说如果你愿意删掉这一栏，王庭会追加预算；你们都知道钱也无法取消误差。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

广场要求在日出前处决所有旧官员。维克把一把斧头放在你面前，承认其中有无辜的人，但认为新秩序需要一场不会反悔的胜利。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

玛伦所在的审判队与撤离队在山口重逢。双方没有握手，却愿意互换值夜。她说自己不需要清白的结局，只需要今晚别再让别人替她承担命令。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

瑟文把权杖放在空椅上，说祝福只表示有人陪伴，不能抹去昨天的伤害。枢机仍要求一个统一口径，外面的信徒则在问他们是否有资格说不。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

分配意志准确说出了你最不愿失去之人的名字。它愿用陌生人的痛苦换这个人的安全。伊芙确认这不是幻觉，却无法证明说话者只是机器或真正的神。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

艾德里安已经不能分清屋外是敌军还是春雨。他仍能回答一个问题：若新世界必须让某人永远醒着，他是否愿意再等。他说，愿意不是永远有效的签名。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

伊芙让还能走动的人决定自己是否撤离。留在病房的人有信徒，也有不信神的人。药品已经按实际存量公开，没有人被许诺一定能活过明天。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

封印椅已经按照你的身形调整。无论你有没有黎明，银管都会寻找一个愿意承压的生命。阿瑟兰提醒你，成为容器不是加冕，痛苦也不会自动证明你正确。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

缇尔把能做到的和做不到的分别写在两页纸上：能停止单人囚禁，不能让所有人从此免于痛苦。每个接口旁都留了一个开关，不再只有中央能够决定。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

体内的回流不再只索要食物，而是索要命令。它愿让你成为最有效率的王，也愿把你塑成所有人都害怕的屏障。没有一种力量会替你决定该伤害谁。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {"Dragons": 1}, "add_flags": ["claimed_abyss"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "下一日获得夺火者的入口；行为永久保留在弧光与结局证据中。"}`

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

龙巢、医院与村庄派来最后一批守门者。每个人都希望你替他们保证明天，但你没有那样的资格。缇尔把备用钥匙交给最年轻的守门人，而不是最强的。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

你召集的议事会终于不再等你发言。有人支持分流，有人主张撤离，第三个人提出先保存种子。托马把你的椅子移到与大家相同的位置。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

萨德在最后一块船板上写了维修方法，而不是自己的名字。水面映着王都熄灭的灯。渡口能做的不是击败魔王，是确保有人活着走到下一个早晨。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

安全领的门再次打开。守卫允许你入城，不再索要旧友名单，只要求放下武器。你终于得到曾经想要的退路，也终于知道退路之外有人仍在等待。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

锅里的汤已经分到最后一碗。家人没有要求你再救任何人，也没有原谅你所有的离开。托马把修好的家钥匙放回你的掌心：无论明天你是什么，今晚仍是家里的人。第六日，钟声终于停了。远处的维护队仍在工作，但没有人能把你的承诺替你完成。今晚的安排会决定明天你能够抵达的地方：进入核心、保住通道，或者给自己和别人留下一条退路。

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

王都只剩最后一轮有效命令。摄政的空椅、候选者的签名与关闭一半的城门都在等你的手。拿过权力并不意味着只能留下它，拒绝它也不能让已经签出的命令消失。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_oath_3 / d6_c_ledger_2 / d6_h_ledger_3 / d6_v_oath_4

### d7_c_oath_1 · 戴上王冠，将封印维护纳入公开国法。

当下理解：王国保留统一调度，同时接受：你必须接受长期问责。

实际后果：王国保留统一调度；你必须接受长期问责。

下一节点：None；终局身份：king

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "终局身份为国王；前六天人格与罪责继续覆盖称号。"}`

### d7_c_oath_2 · 用王令组织自愿缓冲，亲自进入承压椅。

当下理解：旧容器得以休息，同时接受：你的身体成为新的封印。

实际后果：旧容器得以休息；你的身体成为新的封印。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_c_oath_3 · 撤掉宫墙护盾，先保住中央撤离走廊。

当下理解：致命峰值被导离人口核心，同时接受：王宫不可保全。

实际后果：致命峰值被导离人口核心；王宫不可保全。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_c_oath_4 · 交还御印，随最后一队难民走出城门。

当下理解：你的命令留下后果，同时接受：你以普通队员完成护送。

实际后果：你的命令留下后果；你以普通队员完成护送。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["refused_crown"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

## d7_c_ledger · 最后一笔预算

资金、药物与寿命已经写在同一张账上。维克没有填入胜利两个字，奥伦在空栏写了“由谁复核”。系统等着的不是一个不会算错的人，而是肯承认误差的人。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_ledger_1

### d7_c_ledger_1 · 按公开模型分流，保存所有失误记录。

当下理解：最大冲击被削弱，同时接受：受损街区仍需赔偿。

实际后果：最大冲击被削弱；受损街区仍需赔偿。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_c_ledger_2 · 把账目交给共同议会，自己留守水闸。

当下理解：本地安全得到维持，同时接受：你失去全局指挥。

实际后果：本地安全得到维持；你失去全局指挥。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["held_gate_final"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_ledger_3 · 接管国库与维修权，以统一预算重建王国。

当下理解：工程可以延续，同时接受：财政权集中到你手里。

实际后果：工程可以延续；财政权集中到你手里。

下一节点：None；终局身份：king

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["ambition"], "long_term": "终局身份为国王；前六天人格与罪责继续覆盖称号。"}`

### d7_c_ledger_4 · 保全原始账簿，带幸存者离开无法再守的城。

当下理解：真相得以传递，同时接受：城墙最终被放弃。

实际后果：真相得以传递；城墙最终被放弃。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

## d7_c_revolt · 刑台与议事桌

人群等你宣布胜利。刑台还没有拆，议事桌已经摆好；同一批木匠造了它们。深渊不会因为旗帜换色而停止，但它的力量可以替任何掌权者让广场安静。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_revolt_2

### d7_c_revolt_1 · 把强制回路接到刑台，建立服从你的秩序。

当下理解：中央秩序恢复，同时接受：自由被写成需要许可的恩典。

实际后果：中央秩序恢复；自由被写成需要许可的恩典。

下一节点：None；终局身份：tyrant

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"People": -2, "Companions": -1}, "add_flags": ["enslaved_core"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "终局身份为暴君；前六天人格与罪责继续覆盖称号。"}`

### d7_c_revolt_2 · 拆掉刑台，把木料送去修撤离浮桥。

当下理解：惩罚被延后，同时接受：人群获得通行的道路。

实际后果：惩罚被延后；人群获得通行的道路。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["dismantled_scaffold"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_revolt_3 · 关闭以神谕征用人的核心，承认协调能力也会失去。

当下理解：强制神谕终止，同时接受：各地必须共同承担失序。

实际后果：强制神谕终止；各地必须共同承担失序。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_revolt_4 · 接受公开选举的临时王位，立刻交出审判权。

当下理解：权力有了监督，同时接受：新制度仍可能失败。

实际后果：权力有了监督；新制度仍可能失败。

下一节点：None；终局身份：king

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为国王；前六天人格与罪责继续覆盖称号。"}`

## d7_c_guard · 路的尽头还有人

撤离队已经看不见王都。玛伦把最后一面盾靠在路边，告诉你山口之后没有观众，也没有能为今晚重新命名的史官。你可以带人过去，也可以留下来。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_oath_4 / d6_c_revolt_4 / d6_c_guard_2 / d6_w_revolt_4 / d6_v_oath_2 / d6_v_revolt_2 / d6_v_guard_2

### d7_c_guard_1 · 带最后一队伤者穿过山口，然后放下武器。

当下理解：这一队人活着抵达，同时接受：你无法保证远处的城。

实际后果：这一队人活着抵达；你无法保证远处的城。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["escorted_last"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_guard_2 · 留下守住山口，让同行者全部先走。

当下理解：队伍脱离追来的黑潮，同时接受：你没有走出山口。

实际后果：队伍脱离追来的黑潮；你没有走出山口。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_guard_3 · 驻守新的边界，让这里永远接纳后来者。

当下理解：流民得到庇护，同时接受：守望将占据你此后的人生。

实际后果：流民得到庇护；守望将占据你此后的人生。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["founded_border_watch"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_guard_4 · 将指挥交给玛伦，独自寻找失联的村庄。

当下理解：你放弃稳定归宿，同时接受：无人照管的地方仍有人抵达。

实际后果：你放弃稳定归宿；无人照管的地方仍有人抵达。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为远行者；前六天人格与罪责继续覆盖称号。"}`

## d7_h_oath · 祷词之后的回答

最后一次钟声并不比人的声音更响。信徒等待仪式，候选者等待确认，瑟文等待有人允许他只做一个老人。仪式能组织人，也能再次遮住人的脸。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_oath_1 / d6_h_oath_1

### d7_h_oath_1 · 接下权杖，把拒绝与退出写成不可删改的教律。

当下理解：教会继续存在，同时接受：改革必须日复一日执行。

实际后果：教会继续存在；改革必须日复一日执行。

下一节点：None；终局身份：pontiff

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为教会领袖；前六天人格与罪责继续覆盖称号。"}`

### d7_h_oath_2 · 自愿接替旧容器，并让见证人定期复核同意。

当下理解：封印获得延续，同时接受：你承担漫长的痛苦。

实际后果：封印获得延续；你承担漫长的痛苦。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_h_oath_3 · 让圣堂供能转向撤离屏障，接受祭坛崩塌。

当下理解：人群越过危险峰值，同时接受：圣堂失去象征中心。

实际后果：人群越过危险峰值；圣堂失去象征中心。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_h_oath_4 · 拒绝就职，带着仍愿同行的人走出圣堂。

当下理解：信仰回到个人，同时接受：教会暂失统一领导。

实际后果：信仰回到个人；教会暂失统一领导。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["rejected_church"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

## d7_h_ledger · 不可删去的一页

原件、病历与艾德里安的声音都已存档。现在不是再找到一条秘密就能避免决定的时刻。你可以保存知识，可以改变神谕，也可以承认知识无法替任何人同意。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_revolt_1 / d6_h_oath_2 / d6_h_revolt_4

### d7_h_ledger_1 · 永久停用强制神谕核心，保存其计算档案。

当下理解：强制征用终止，同时接受：失去中央协调造成长期困难。

实际后果：强制征用终止；失去中央协调造成长期困难。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为弑神者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_ledger_2 · 成立独立记忆馆，陪证人离开封印城。

当下理解：篡改不再容易，同时接受：你没有亲自终结黑潮。

实际后果：篡改不再容易；你没有亲自终结黑潮。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_ledger_3 · 保留仪式，接管教会并开放所有原始档案。

当下理解：信徒仍有共同组织，同时接受：公开真相引发分裂。

实际后果：信徒仍有共同组织；公开真相引发分裂。

下一节点：None；终局身份：pontiff

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为教会领袖；前六天人格与罪责继续覆盖称号。"}`

### d7_h_ledger_4 · 把自己的记忆接入缓冲层，为维修队争到时间。

当下理解：维修得以完成一轮，同时接受：你的人格不能完整回来。

实际后果：维修得以完成一轮；你的人格不能完整回来。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

## d7_h_revolt · 魔王最后的名字

艾德里安请你别在最后仍称他为魔王。他允许别人不同意他的选择，却不愿再被塑成不会疲惫的象征。屋外两族的声音交叠，听起来都像害怕失去家的人。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_guard_1 / d6_h_oath_3 / d6_h_ledger_1

### d7_h_revolt_1 · 接替艾德里安，公开承认魔王是一份职责。

当下理解：旧勇者得以休息，同时接受：偏见不会随公告消失。

实际后果：旧勇者得以休息；偏见不会随公告消失。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_h_revolt_2 · 断开强制神谕，与两族共同维护余下的封印。

当下理解：奴役接口被关闭，同时接受：维护成本由社会承担。

实际后果：奴役接口被关闭；维护成本由社会承担。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_revolt_3 · 尊重他的停止请求，将余压导入预留缓冲。

当下理解：艾德里安平静死去，同时接受：缓冲为居民争到存续时间。

实际后果：艾德里安平静死去；缓冲为居民争到存续时间。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["released_previous_hero"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_h_revolt_4 · 带走他的证词，护送病房里的平民离城。

当下理解：历史有了幸存证人，同时接受：封印由留下的人接手。

实际后果：历史有了幸存证人；封印由留下的人接手。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

## d7_h_guard · 病房门外的黎明

伊芙洗净最后一双手套，问你要不要一起把床推出去。没有人会在史诗里完整写下转运一张床需要多少次停顿，但床上的人会记得经过的每一扇门。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_revolt_3 / d6_h_revolt_2 / d6_h_guard_1 / d6_w_revolt_3 / d6_v_ledger_4

### d7_h_guard_1 · 接下医院的终身守护契约，拒绝军事征用。

当下理解：伤者有了中立家园，同时接受：守护并不等于没有敌人。

实际后果：伤者有了中立家园；守护并不等于没有敌人。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["protected_hospital"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_guard_2 · 把病床编成船队，亲自带到安全岸。

当下理解：病人跨过黑潮支流，同时接受：物资只能留在原处。

实际后果：病人跨过黑潮支流；物资只能留在原处。

下一节点：None；终局身份：ferryman

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["ferried_beds"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为摆渡人；前六天人格与罪责继续覆盖称号。"}`

### d7_h_guard_3 · 留在最后一盏灯下，以生命维持重症屏障。

当下理解：重症者等到撤离，同时接受：你在灯熄后死去。

实际后果：重症者等到撤离；你在灯熄后死去。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_guard_4 · 拒绝任何职务，回村照料幸存的邻人。

当下理解：你保有一段普通生活，同时接受：世界的修复不会因此完成。

实际后果：你保有一段普通生活；世界的修复不会因此完成。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为普通人；前六天人格与罪责继续覆盖称号。"}`

## d7_w_oath · 椅子不是王座

封印椅发出木头开裂的声音。黎明的传说在你耳中逐渐远去，留下的是一个生命是否愿意继续的简单问题。你没有得到纯洁证明，也没有失去重新选择的资格。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_ledger_3 / d6_h_oath_4 / d6_h_ledger_4 / d6_h_revolt_1 / d6_w_oath_1 / d6_w_ledger_2 / d6_w_guard_4

### d7_w_oath_1 · 坐进承压椅，接下有期限的魔王职责。

当下理解：大陆获得下一段时间，同时接受：继任问题没有消失。

实际后果：大陆获得下一段时间；继任问题没有消失。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_w_oath_2 · 站在外环承担第一轮黑潮，掩护所有值守者退后。

当下理解：维护者保存下来，同时接受：你的生命耗尽。

实际后果：维护者保存下来；你的生命耗尽。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_oath_3 · 以承压训练稳定峰值，再把维护交给共同守望队。

当下理解：最危险的一轮过去，同时接受：长期维护仍需要众人。

实际后果：最危险的一轮过去；长期维护仍需要众人。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_w_oath_4 · 将封印外门改成共同哨所，与龙族轮值。

当下理解：守门职责不再独占，同时接受：休息必须以他人的接班换来。

实际后果：守门职责不再独占；休息必须以他人的接班换来。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["shared_watch_final"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

## d7_w_ledger · 图纸外的一毫米

最后一枚接头偏离图纸一毫米。缇尔没有隐瞒，工匠们因此多绕了一段铜线。技术拯救人的方式并不总像奇迹，有时只是有人把误差讲了出来。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_oath_2 / d6_h_ledger_2 / d6_w_oath_2 / d6_v_revolt_4

### d7_w_ledger_1 · 启动经现场复核的分流，把灾难峰值引向空域。

当下理解：大陆避过即时崩塌，同时接受：污染与维修债留给生者。

实际后果：大陆避过即时崩塌；污染与维修债留给生者。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["saved_continent"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_w_ledger_2 · 拆除强制分配中枢，让接口从此只能自愿接入。

当下理解：旧神谕的权力终止，同时接受：新秩序需要重新协商。

实际后果：旧神谕的权力终止；新秩序需要重新协商。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_ledger_3 · 把最后的过载引进自己，保住维修人员。

当下理解：图纸有人继续执行，同时接受：你不能看见完成的系统。

实际后果：图纸有人继续执行；你不能看见完成的系统。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_ledger_4 · 保存开源图纸，踏上寻找失联节点的道路。

当下理解：知识随你流动，同时接受：你失去安稳归宿。

实际后果：知识随你流动；你失去安稳归宿。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为远行者；前六天人格与罪责继续覆盖称号。"}`

## d7_w_revolt · 没有人能命令你

深渊的声音愿意服从，条件是你永远不要松手。你第一次拥有足够改变许多人命运的力量，也第一次发现，没有上级并不意味着没有责任。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_w_ledger_4 / d6_w_revolt_2

### d7_w_revolt_1 · 独占核心，以恐惧维持一座不会反抗的城。

当下理解：城内暂时安定，同时接受：居民的意志成为燃料。

实际后果：城内暂时安定；居民的意志成为燃料。

下一节点：None；终局身份：tyrant

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 5, "Mercy": -1}, "relationship_change": {"People": -2, "Companions": -1}, "add_flags": ["enslaved_core"], "remove_flags": [], "arc_tags": ["corruption", "harm"], "long_term": "终局身份为暴君；前六天人格与罪责继续覆盖称号。"}`

### d7_w_revolt_2 · 把力量封入自己的身体，停止向他人索取。

当下理解：黑潮有了新容器，同时接受：你无法轻易走出封印。

实际后果：黑潮有了新容器；你无法轻易走出封印。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_w_revolt_3 · 用残余力量撕开撤离通道，然后交出控制器。

当下理解：人群得救，同时接受：你必须面对此前的伤害。

实际后果：人群得救；你必须面对此前的伤害。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["surrendered_power_final"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_revolt_4 · 拒绝任何限制，向黑潮索取超过身体的力量。

当下理解：力量越过容器极限，同时接受：附近的屏障随你一起破裂。

实际后果：力量越过容器极限；附近的屏障随你一起破裂。

下一节点：None；终局身份：failed

策划效果：`{"primary": "Corruption", "stat_change": {"Corruption": 3}, "relationship_change": {}, "add_flags": ["lost_self"], "remove_flags": [], "arc_tags": ["corruption"], "long_term": "终局身份为失控者；前六天人格与罪责继续覆盖称号。"}`

## d7_w_guard · 鳞片与炊烟

幼龙的呼吸不再急促，难民营里升起第一缕炊烟。阿瑟兰说它能守山，却不懂如何让被火伤过的人愿意回来。那不是任何契约能一次完成的工作。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_w_oath_3 / d6_w_revolt_1 / d6_w_guard_1

### d7_w_guard_1 · 成为两族照护人的一员，守护龙巢与周边村庄。

当下理解：共居开始，同时接受：双方仍需面对旧伤。

实际后果：共居开始；双方仍需面对旧伤。

下一节点：None；终局身份：dragonkeeper

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {"Dragons": 2}, "add_flags": ["kept_dragon_care"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为养龙人；前六天人格与罪责继续覆盖称号。"}`

### d7_w_guard_2 · 把龙巢护盾留给病人，自己守住破损外墙。

当下理解：弱者获得保护，同时接受：你把余生留在边界。

实际后果：弱者获得保护；你把余生留在边界。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["held_gate_final"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_guard_3 · 与龙族签公开轮值约，接下第一期容器职责。

当下理解：封印延续，同时接受：龙族不能再置身事外。

实际后果：封印延续；龙族不能再置身事外。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_w_guard_4 · 放下看守权，护送幼龙与孩子去新的栖地。

当下理解：孩子不再继承旧战场，同时接受：你也告别熟悉的家。

实际后果：孩子不再继承旧战场；你也告别熟悉的家。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为远行者；前六天人格与罪责继续覆盖称号。"}`

## d7_v_oath · 你的椅子也是木头

议事会没有为你准备宝座，只添了一张和大家一样的椅子。共同承压需要签名，最后的道路需要看守，明天的饭需要种子。没有一项能替代另外两项。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_guard_3 / d6_h_guard_4 / d6_w_oath_4 / d6_w_ledger_3 / d6_v_ledger_2 / d6_v_guard_4

### d7_v_oath_1 · 签下共同维护协议，亲自参加第一轮承压。

当下理解：灾难峰值得到分担，同时接受：人人仍有长期责任。

实际后果：灾难峰值得到分担；人人仍有长期责任。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["collective_final"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_v_oath_2 · 归还代表徽记，以邻居身份开始重建。

当下理解：你回到日常，同时接受：制度由其他代表继续维护。

实际后果：你回到日常；制度由其他代表继续维护。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为普通人；前六天人格与罪责继续覆盖称号。"}`

### d7_v_oath_3 · 接受限期执政职位，把交权日期刻在印玺上。

当下理解：调度得到延续，同时接受：日期能否兑现仍需监督。

实际后果：调度得到延续；日期能否兑现仍需监督。

下一节点：None；终局身份：king

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为国王；前六天人格与罪责继续覆盖称号。"}`

### d7_v_oath_4 · 拒绝王位，带民兵守到最后一名撤离者过桥。

当下理解：桥上无人被独留，同时接受：你付出伤病与时间。

实际后果：桥上无人被独留；你付出伤病与时间。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["escorted_last"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

## d7_v_ledger · 让明天不再需要一个人

渡口与分压网络同时传来信号。若试验和同意都已落实，这里能接回被转移了七百年的代价；否则它只能帮世界多撑过一次洪峰。没有人可以用愿望代替那些准备。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_guard_4 / d6_h_guard_2 / d6_w_ledger_1 / d6_w_guard_2 / d6_v_oath_1 / d6_v_ledger_1 / d6_v_guard_3

### d7_v_ledger_1 · 接通自愿分压网络，把开关留在每个居民手中。

当下理解：按前置验证决定长期转型或短期稳压，同时接受：生活将失去旧文明的便利。

实际后果：按前置验证决定长期转型或短期稳压；生活将失去旧文明的便利。

下一节点：None；终局身份：savior

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["collective_final"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为救世主；前六天人格与罪责继续覆盖称号。"}`

### d7_v_ledger_2 · 不冒险扩大系统，完成最后一轮渡运。

当下理解：岸边的人得救，同时接受：大陆封印由别处继续维护。

实际后果：岸边的人得救；大陆封印由别处继续维护。

下一节点：None；终局身份：ferryman

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["ferried_last"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为摆渡人；前六天人格与罪责继续覆盖称号。"}`

### d7_v_ledger_3 · 把船位让给同伴，自己留在闸底扳住手轮。

当下理解：同伴得以离开，同时接受：水压最终夺去你的生命。

实际后果：同伴得以离开；水压最终夺去你的生命。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

### d7_v_ledger_4 · 保存水路与维修图，带证人去安全领。

当下理解：下一次灾难不必从零开始，同时接受：你离开故乡。

实际后果：下一次灾难不必从零开始；你离开故乡。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

## d7_v_revolt · 门在你身后关上

安全领允许你登记一个新的职业，不必写下英雄或逃兵。你知道墙外还有未结束的事，也知道活着并不是一件自动获得赦免的事。桌上只有纸、灯和一把普通钥匙。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_v_revolt_1

### d7_v_revolt_1 · 登记为居民，认真活完这段被争取来的日常。

当下理解：你开始新生活，同时接受：离开的人仍可能责怪你。

实际后果：你开始新生活；离开的人仍可能责怪你。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为普通人；前六天人格与罪责继续覆盖称号。"}`

### d7_v_revolt_2 · 承认离开战场，拒绝接受任何追授的荣耀。

当下理解：身份诚实，同时接受：你失去方便的英雄叙事。

实际后果：身份诚实；你失去方便的英雄叙事。

下一节点：None；终局身份：exile

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["accepted_exile"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为流亡者；前六天人格与罪责继续覆盖称号。"}`

### d7_v_revolt_3 · 写下所有见闻，包括自己没能回去的那一天。

当下理解：记录留下缺口与羞耻，同时接受：真相不再只由赢家书写。

实际后果：记录留下缺口与羞耻；真相不再只由赢家书写。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

### d7_v_revolt_4 · 离开安全领，去那些没有出现在地图上的地方。

当下理解：你再次承担未知，同时接受：没有人许诺你的回归。

实际后果：你再次承担未知；没有人许诺你的回归。

下一节点：None；终局身份：wanderer

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["walked_unmapped"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为远行者；前六天人格与罪责继续覆盖称号。"}`

## d7_v_guard · 第七碗汤

远处的光没有告诉你谁赢了。邻人带来一把种子，孩子把门上的裂缝用布塞好。你等了七天的最后问题，原来不是谁来称你勇者，而是接下来这碗汤端给谁。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_ledger_4 / d6_h_revolt_3 / d6_h_guard_3 / d6_w_guard_3 / d6_v_oath_3 / d6_v_ledger_3 / d6_v_revolt_3 / d6_v_guard_1

### d7_v_guard_1 · 留在故乡，照顾活下来的人并承认自己的限度。

当下理解：日常重新开始，同时接受：失去的人不会因此回来。

实际后果：日常重新开始；失去的人不会因此回来。

下一节点：None；终局身份：ordinary

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["chose_ordinary_life"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为普通人；前六天人格与罪责继续覆盖称号。"}`

### d7_v_guard_2 · 沿河撑船，把汤和药送给还未过岸的人。

当下理解：河岸得到接应，同时接受：你再次离开家门。

实际后果：河岸得到接应；你再次离开家门。

下一节点：None；终局身份：ferryman

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["ferried_last"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为摆渡人；前六天人格与罪责继续覆盖称号。"}`

### d7_v_guard_3 · 守在外堤，让村里的人安睡第一夜。

当下理解：故乡得到缓冲，同时接受：你的守望还未结束。

实际后果：故乡得到缓冲；你的守望还未结束。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["held_gate_final"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

### d7_v_guard_4 · 将龙族与人类留下的孩子一起养大。

当下理解：新一代有了共同的家，同时接受：旧社会未必欢迎它。

实际后果：新一代有了共同的家；旧社会未必欢迎它。

下一节点：None；终局身份：dragonkeeper

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {"Dragons": 2}, "add_flags": ["kept_dragon_care"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为养龙人；前六天人格与罪责继续覆盖称号。"}`

## d7_w_oath_sword · 黎明的四种用途

圣剑仍在你的手里。它能切开强制回路，也能充当导流针，能够让军队听令，却不能替任何一种用途证明正当。你已经接受过失去生命的可能；这不等于今天必须交出自己的判断。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_ledger_3 / d6_h_oath_4 / d6_h_ledger_4 / d6_h_revolt_1 / d6_w_oath_1 / d6_w_ledger_2 / d6_w_guard_4

### d7_w_oath_sword_1 · 将黎明化为导流针，自愿接替旧容器。

当下理解：圣剑进入封印而非王座，同时接受：你的生命成为承压边界。

实际后果：圣剑进入封印而非王座；你的生命成为承压边界。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

### d7_w_oath_sword_2 · 用黎明切断神谕征用接口，保留人工维护回路。

当下理解：强制征用被终止，同时接受：圣剑永久失去完整剑身。

实际后果：强制征用被终止；圣剑永久失去完整剑身。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_oath_sword_3 · 将黎明举作停火信号，护送两族伤者离开。

当下理解：威望被用来停止追杀，同时接受：你放弃亲自统治核心。

实际后果：威望被用来停止追杀；你放弃亲自统治核心。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Mercy", "stat_change": {"Mercy": 3}, "relationship_change": {}, "add_flags": ["sword_as_signal"], "remove_flags": [], "arc_tags": ["mercy"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_oath_sword_4 · 折断黎明释放一次屏障，自己守住崩裂缺口。

当下理解：众人得到撤离窗口，同时接受：你与圣剑一同留在缺口。

实际后果：众人得到撤离窗口；你与圣剑一同留在缺口。

下一节点：None；终局身份：martyr

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["sacrificed_self"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为殉道者；前六天人格与罪责继续覆盖称号。"}`

## d7_w_guard_dragon_debt · 没有古龙签名的契约

龙族遗誓使带来阿瑟兰的遗骨，没有带来宽恕。护卵与共同照护仍然可以继续，但你不能替死者签下和解。门外有受过你帮助的人，也有认得你手上龙血的人。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_w_oath_3 / d6_w_revolt_1 / d6_w_guard_1

### d7_w_guard_dragon_debt_1 · 接受监督，守住受损龙境并长期偿还赔偿。

当下理解：边界得到保护，同时接受：你不再拥有自由离开的权利。

实际后果：边界得到保护；你不再拥有自由离开的权利。

下一节点：None；终局身份：guardian

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["accepted_dragon_reparation"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为守护者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_guard_dragon_debt_2 · 交出全部屠龙记录，让两族分别保存证词。

当下理解：死亡不会被功绩隐去，同时接受：你接受公开审查。

实际后果：死亡不会被功绩隐去；你接受公开审查。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_guard_dragon_debt_3 · 把幼龙交给共同照护会，接受永久离境。

当下理解：幼龙不必由杀死父亲的人监护，同时接受：你失去归处。

实际后果：幼龙不必由杀死父亲的人监护；你失去归处。

下一节点：None；终局身份：exile

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["accepted_exile"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为流亡者；前六天人格与罪责继续覆盖称号。"}`

### d7_w_guard_dragon_debt_4 · 以新的容器职责补上失去的承压支点。

当下理解：灾难得到一次缓冲，同时接受：这不是对屠龙的自动赦免。

实际后果：灾难得到一次缓冲；这不是对屠龙的自动赦免。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`

## d7_c_oath_judgment · 加冕之前，先读出名单

原本准备加冕的长桌上摆满了受害者名单。莱娅没有阻止他们入场，卫队也没有替你清空道路。你仍握着印玺，却不再能把所有人的沉默误认为同意。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_oath_3 / d6_c_ledger_2 / d6_h_ledger_3 / d6_v_oath_4

### d7_c_oath_judgment_1 · 接受有独立审判监督的王位，公开承担旧令责任。

当下理解：王国保有调度，同时接受：你的罪责不受王位豁免。

实际后果：王国保有调度；你的罪责不受王位豁免。

下一节点：None；终局身份：king

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["accepted_crown"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为国王；前六天人格与罪责继续覆盖称号。"}`

### d7_c_oath_judgment_2 · 交出印玺，先完成受害者要求的撤离任务。

当下理解：一批人获得救援，同时接受：你不能据此要求撤回控诉。

实际后果：一批人获得救援；你不能据此要求撤回控诉。

下一节点：None；终局身份：hero

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["submitted_to_victims"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为勇者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_oath_judgment_3 · 签下自己的供词，把证据送出王都。

当下理解：证据不再受你控制，同时接受：王位可能由对手取得。

实际后果：证据不再受你控制；王位可能由对手取得。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Courage", "stat_change": {"Courage": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["courage"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

### d7_c_oath_judgment_4 · 让卫队驱逐证人，以封印危机为由永不交权。

当下理解：你的命令不再被打断，同时接受：受害者失去拒绝的权利。

实际后果：你的命令不再被打断；受害者失去拒绝的权利。

下一节点：None；终局身份：tyrant

策划效果：`{"primary": "Ambition", "stat_change": {"Ambition": 3, "Corruption": 2, "Mercy": -1}, "relationship_change": {"People": -2, "Companions": -1}, "add_flags": ["enslaved_core"], "remove_flags": [], "arc_tags": ["ambition", "harm"], "long_term": "终局身份为暴君；前六天人格与罪责继续覆盖称号。"}`

## d7_h_oath_dissent · 曾经离开的人回来了

你曾公开拒绝教会，如今却再次站在圣堂门内。枢机不能把你的返回写作认错，因为你没有撤回当初的质询。信徒在等你说明哪些东西还值得保留，哪些不能再以神的名义继续。第七日，世界没有为所有人准备同一座王座。你来到的这一处终点，是前六天的行动真正留下的入口。今天可以决定你愿意怎样结束这段旅程，却无法把此前的伤害、救助与缺席一笔勾销。

前置：d6_c_oath_1 / d6_h_oath_1

### d7_h_oath_dissent_1 · 以异议者身份接任，确立任何人都能退出的教律。

当下理解：信仰与质询暂时共处，同时接受：顽固派拒绝承认你。

实际后果：信仰与质询暂时共处；顽固派拒绝承认你。

下一节点：None；终局身份：pontiff

策划效果：`{"primary": "Faith", "stat_change": {"Faith": 3}, "relationship_change": {}, "add_flags": ["accepted_crosier"], "remove_flags": [], "arc_tags": ["faith"], "long_term": "终局身份为教会领袖；前六天人格与罪责继续覆盖称号。"}`

### d7_h_oath_dissent_2 · 关闭强制神谕，让圣堂转为自愿救助组织。

当下理解：征用人的权力终止，同时接受：统一神谕也不再存在。

实际后果：征用人的权力终止；统一神谕也不再存在。

下一节点：None；终局身份：godslayer

策划效果：`{"primary": "Freedom", "stat_change": {"Freedom": 3}, "relationship_change": {}, "add_flags": ["killed_oracle"], "remove_flags": [], "arc_tags": ["freedom"], "long_term": "终局身份为弑神者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_oath_dissent_3 · 拒绝权杖，保存教会的功绩与罪行原件。

当下理解：历史不再只有颂歌或控诉，同时接受：你失去改革的职位。

实际后果：历史不再只有颂歌或控诉；你失去改革的职位。

下一节点：None；终局身份：witness

策划效果：`{"primary": "Reason", "stat_change": {"Reason": 3}, "relationship_change": {}, "add_flags": ["preserved_records"], "remove_flags": [], "arc_tags": ["reason"], "long_term": "终局身份为见证者；前六天人格与罪责继续覆盖称号。"}`

### d7_h_oath_dissent_4 · 不向教会效忠，只以个人身份接受容器交接。

当下理解：封印得到延续，同时接受：你的同意不属于任何神职者。

实际后果：封印得到延续；你的同意不属于任何神职者。

下一节点：None；终局身份：vessel

策划效果：`{"primary": "Sacrifice", "stat_change": {"Sacrifice": 3}, "relationship_change": {"Companions": 1}, "add_flags": ["became_demon_king"], "remove_flags": [], "arc_tags": ["sacrifice"], "long_term": "终局身份为魔王；前六天人格与罪责继续覆盖称号。"}`