# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:06:39 2024

@author: Anonymous
"""

acquire_num_dict= {"四七六二九":"乾卦，潛龍勿用。",
"四八三九八":"乾卦，見龍在田利見大人",
"四九一六七":"乾卦，君子終日乾乾夕惕若厲无咎",
"三六一一二":"乾卦，或躍在淵无咎",
"四三七九三":"乾卦，飛龍在天",
"五一四七四":"乾卦，亢龍有悔",
"一四七八九":"坤卦，履霜堅冰至",
"一五四六二":"坤卦，直方大不習无不利",
"一六一三五":"坤卦，含章可貞或從王事无成有終",
"二八九Ｏ四":"坤卦，括囊无咎无譽",
"三五六二五":"坤卦，黃裳元吉",
"四二三四六":"坤卦，龍戰于野其血玄黃",
"二二五三三":"屯卦，元亨利貞勿用有攸往利建侯",
"二二五三三":"屯卦，磐桓利居貞利建侯",
"二三二三八":"屯卦，乘馬班如屯如邅如匪寇婚媾女子貞不字十年乃字",
"二三九四三":"屯卦，即鹿无虞惟入于林中君子幾不如舍往吝",
"二九五七六":"屯卦，乘馬班如求婚媾往吉无不利",
"三六六一七":"屯卦，屯其膏小貞吉大貞凶",
"四三六五八":"屯卦，乘馬班如泣血漣如",
"Ｏ八四五八":"蒙卦，發蒙利用刑人用說桎梏以往吝",
"Ｏ九一六三":"蒙卦，包蒙吉納婦吉子克家",
"Ｏ九八六八":"蒙卦，勿用取女見金夫不有躬无攸利",
"三四五Ｏ九":"蒙卦，困蒙吝",
"四一五五Ｏ":"蒙卦，童蒙吉",
"四八五九一":"蒙卦，擊蒙不利為寇利禦寇",
"四五六四Ｏ":"需卦，需于郊利用恆无咎",
"四六三七七":"需卦，需于沙小有言終吉",
"四七一一四":"需卦，需于泥致寇至",
"三Ｏ九二三":"需卦，需于血出自穴",
"三八二八四":"需卦，需于酒食貞吉",
"四五六四五":"需卦，入于穴有不速之客三人來敬之无咎",
"Ｏ八八四Ｏ":"訟卦，不永所事小有言終吉",
"Ｏ九五七七":"訟卦，不克訟歸而逋邑人三百戶无眚",
"二Ｏ三一四":"訟卦，食舊德貞厲終吉或從王事无成",
"一四六Ｏ三":"訟卦，不克訟復即命渝安貞吉",
"一九六四Ｏ":"訟卦，訟元吉",
"四九三二五":"訟卦，或錫之鞶帶終朝三褫之",
"Ｏ八二六Ｏ":"師卦，師出以律否臧凶",
"Ｏ八九四九":"師卦，在師中吉无咎王三錫命",
"Ｏ九六三八":"師卦，師或輿尸凶",
"二九五九一":"師卦，師左次无咎",
"三六四七二":"師卦，田有禽利執言无咎長子帥師",
"四二三五三":"師卦，大君有命開國承家小人勿用",
"一五一四Ｏ":"比卦，有孚比之无咎有孚盈缶終來有他吉",
"一五八二九":"比卦，比之自內貞吉",
"一六五一八":"比卦，比之匪人",
"一八九Ｏ三":"比卦，外比之貞吉",
"三五七八四":"比卦，顯比王用三驅失前禽邑人不誡吉",
"四二六六五":"比卦，比之无首凶",
"四六六三五":"小畜卦，復自道何其咎吉",  
"四七三八八":"小畜卦，牽復吉",  
"四八一四一":"小畜卦，輿說輻夫妻反目",
"三三八Ｏ九":"小畜卦，有孚血出惕",
"四一三七Ｏ":"小畜卦，有孚攣如富以其鄰",
"四八八九一":"小畜卦，既雨既處尚德載婦貞厲月幾望君子征凶",
"五四一五八":"履卦，素履往无咎",
"五四九一一":"履卦，履道坦坦",
"五五六六四":"履卦，眇能視跛能履履虎尾咥人凶",
"三五三六一":"履卦，履虎尾愬愬終吉",
"四二八八二":"履卦，夬履貞厲",
"五Ｏ四Ｏ三":"履卦，視履考祥其旋元吉",
"四四六四九":"泰卦，拔茅茹以其彙征吉",
"四五三七Ｏ":"泰卦，包荒用憑河不遐遺朋亡得尚于中行",
"四六Ｏ九一":"泰卦，无平不陂无往不復艱貞无咎勿恤其孚于食有福",
"三Ｏ九七二":"泰卦，翩翩不富以其鄰不戒以孚",
"三八一七三":"泰卦，帝乙歸妹以祉元吉",
"四五三七四":"泰卦，城復于隍勿用師自邑告命貞吝",
"一五八四九":"否卦，拔茅茹以其彙貞吉亨",
"一六五七Ｏ":"否卦，包承小人吉大人否亨",
"一七二九一":"否卦，包羞",
"二三八五二":"否卦，有命无咎疇離祉",
"四一Ｏ五三":"否卦，休否大人吉其亡其亡係于包桑",
"四八二五四":"否卦，傾否先否後吉",
"六九二ＯＯ":"同人卦，同人于門无咎",
"六九九五三":"同人卦，同人于宗吝",
"七Ｏ七Ｏ六":"同人卦，伏戎于莽升其高陵三歲不興",
"三五三六三":"同人卦，乘其墉弗克攻吉",
"四二八八四":"同人卦，同人先號咷而後笑大師克相遇",
"五Ｏ四Ｏ五":"同人卦，同人于郊無悔",
"四六六四Ｏ":"大有卦，无交害匪咎艱則无咎",
"四七三九三":"大有卦，大車以載有攸往无咎",
"四八一四六":"大有卦，公用亨于天子小人弗克",
"三七六一九":"大有卦，匪其彭无咎",
"四五一四Ｏ":"大有卦，厥孚交如威如吉",
"五二六六一":"大有卦，自天佑之吉无不利",
"五六四二七":"謙卦，謙謙君子用涉大川吉",
"五七一一六":"謙卦，鳴謙貞吉",
"五七八Ｏ五":"謙卦，勞謙君子有終吉",
"一九五九八":"謙卦，无不利撝謙",
"三六四七九":"謙卦，不富以其鄰利用侵伐",
"四三三六Ｏ":"謙卦，鳴謙利用行師征邑國",
"一五一四二":"豫卦，鳴豫凶",
"一五八三一":"豫卦，介于石不終日貞吉",
"一六五ＯＯ":"豫卦，盱豫悔遲有悔",
"三Ｏ二八一":"豫卦，由豫大有得勿疑朋",
"三七一六二":"豫卦，貞疾恒不死",
"四四Ｏ四三":"豫卦，冥豫成有渝",
"二三Ｏ五一":"隨卦，官有渝貞吉出門交有功",
"二三七七二":"隨卦，係小子失丈夫",
"二四四九三":"隨卦，係丈夫失小子隨有求得",
"三四五七四":"隨卦，隨有獲貞凶有孚在道",
"四一七七五":"隨卦，孚于嘉言",
"四八九七六":"隨卦，拘係之乃從維之王用亨于西山",
"三Ｏ二五三":"蠱卦，幹父之蠱有子考无咎厲終吉",
"三Ｏ九七四":"蠱卦，幹母之蠱不可貞",
"三一六九五":"蠱卦，幹父之蠱小有悔无大咎",
"三五二九六":"蠱卦，裕父之蠱往見吝",
"四二四九七":"蠱卦，幹父之蠱用譽",
"四九六九八":"蠱卦，不事王侯高尚其事",
"五Ｏ六九八":"臨卦，咸臨貞吉",
"五一四Ｏ三":"臨卦，咸臨吉无不利",
"五二一Ｏ八":"臨卦，甘臨无攸利既憂之无咎",
"三Ｏ二八五":"臨卦，至臨无咎",
"三七三二六":"臨卦，知臨大君之宜吉",
"四四三六七":"臨卦，敦臨吉无咎",
"一五四九五":"觀卦，童觀小人无咎君子吝",
"一六二ＯＯ":"觀卦，闚觀利女貞",
"一六九Ｏ五":"觀卦，觀我生進退",
"三一六九Ｏ":"觀卦，觀國之光利用賓于王",
"三八七三一":"觀卦，觀我生君子无咎",
"四五七七二":"觀卦，觀其生君子无咎",
"二三Ｏ五三":"噬嗑卦，屨校滅趾无咎",
"二三七七四":"噬嗑卦，噬膚滅鼻无咎",
"二四四九五":"噬嗑卦，噬腊肉遇毒小吝无咎",
"三六Ｏ一六":"噬嗑卦，噬乾胏得金矢利艱",
"四三二一七":"噬嗑卦，噬乾肉得黃金貞厲无咎",
"五Ｏ四一八":"噬嗑卦，何校滅耳凶",
"六六二五八":"賁卦，賁其趾舍車而徒",
"六六九七九":"賁卦，賁其須",
"六七七ＯＯ":"賁卦，賁如濡如永貞吉",
"三五三Ｏ一":"賁卦，賁如皤如白馬翰如匪寇婚媾",
"四二五Ｏ二":"賁卦，賁于丘園束帛箋箋吝終吉",
"四九七Ｏ三":"賁卦，白賁无咎",
"一五一四七":"剝卦，剝牀以足蔑貞凶",
"一五八三六":"剝卦，剝牀以辨蔑貞凶",
"一六五二五":"剝卦，剝之无咎",
"三三七二六":"剝卦，剝牀以膚凶",
"四Ｏ六Ｏ七":"剝卦，貫魚以宮人寵无不利",
"四七四八八":"剝卦，碩果不食君子得輿小人剝廬",
"二二Ｏ二二":"復卦，不遠復无祇悔元吉",
"二二七一一":"復卦，休復吉",
"二三四ＯＯ":"復卦，頻復厲无咎",
"二九五九三":"復卦，中行獨復",
"三六四七四":"復卦，敦復无悔",
"四三三五五":"復卦，迷復凶有灾眚用行師終有大敗以其國君凶至于十年不克征",
"二三五六二":"无妄卦，无妄往吉",
"二四二九九":"无妄卦，不耕獲不菑畬則利有攸往",
"二五Ｏ三六":"无妄卦，无妄之災或係之牛行人之得邑人之災",
"三四六Ｏ五":"无妄卦，可貞无咎",
"四一九六六":"无妄卦，无妄之疾勿藥有喜",
"四九三二七":"无妄卦，无妄行有眚无攸利",
"四五六四七":"大畜卦，有厲利已",
"四六三八四":"大畜卦，輿說輹",
"四七一一Ｏ":"大畜卦，良馬逐利艱貞曰閑輿衛利有攸往",
"三六Ｏ八二":"大畜卦，童牛之牿元吉",
"四三四四二":"大畜卦，豶豕之吉",
"五Ｏ八Ｏ四":"大畜卦，何天之衢亨",
"二二五四Ｏ":"頤卦，舍爾靈龜觀我朵頤凶",
"二三二四五":"頤卦，顛頤拂經于丘頤征凶",
"二三九五Ｏ":"頤卦，拂頤貞凶十年勿用无攸利",
"三四五一一":"頤卦，顛頤吉虎視耽耽其欲逐逐",
"四一五五二":"頤卦，頤經居真吉不可涉大川",
"四八五九三":"頤卦，由頤厲吉利涉大川",
"三Ｏ九二四":"大過卦，藉用白茅无咎",
"三一六六一":"大過卦，枯楊生梯老夫得其女妻无不利",
"三二三九四":"大過卦，棟橈凶",
"三五三四三":"大過卦，棟隆吉有它吝",
"四二七Ｏ四":"大過卦，枯楊生華老婦得其士夫无咎无譽",
"五ＯＯ六五":"大過卦，過涉滅頂凶",
"Ｏ八四五一":"坎卦，習坎入于坎窞凶",
"Ｏ九一五一":"坎卦，坎有險求小得",
"Ｏ九八六六":"坎卦，來之坎坎且枕入于坎窞勿用",
"二九五七四":"坎卦，樽酒簋貳用缶納約自牖終无咎",
"二六六一五":"坎卦，坎不盈祗既平无咎",
"四三六五六":"坎卦，繫于徽纆寘于叢棘三歲不得凶",
"六七七三一":"離卦，履錯然敬之无咎",
"六八四六八":"離卦，黃離元吉",
"六九二Ｏ五":"離卦，日昃之離不鼓缶而歌則大耋之嗟凶",
"三六八二二":"離卦，突如其來如焚如死如棄如",
"四四一八三":"離卦，出涕沱若戚嗟如吉",
"五二五四四":"離卦，王用出征有嘉折首獲匪其醜无咎",
"五九Ｏ五六":"咸卦，咸其拇",
"五九七七七":"咸卦，咸其腓凶居吉",
"六Ｏ四九八":"咸卦，咸其股執其隨往吝",
"三四五七九":"咸卦，貞吉悔亡憧憧往來朋從爾思",
"四一七八Ｏ":"咸卦，咸其脢无悔",
"四八九八一":"咸卦，咸其輔頰舌",
"三Ｏ二四八":"恒卦，浚恒貞凶无攸利",
"三Ｏ九六九":"恒卦，悔亡",
"三一六九Ｏ":"恒卦，不恒其德或承之羞",
"二一六九一":"恒卦，田无禽",
"三八八九二":"恒卦，恒其德貞婦人吉天子凶",
"四六Ｏ九三":"恒卦，振恒凶",
"六Ｏ三六七":"遯卦，遯尾厲勿用有攸往",
"六一一Ｏ四":"遯卦，執之用黃牛之革莫之勝說",
"六一八四一":"遯卦，係遯有疾厲畜臣妾吉",
"三四六一Ｏ":"遯卦，好遯君子吉小人否",
"四一九七一":"遯卦，嘉遯貞吉",
"四九三三二":"遯卦，肥遯无不利",
"四五六四二":"大壯卦，壯于趾征凶有孚",
"四六三七九":"大壯卦，貞吉",
"四七一一六":"大壯卦，小人用壯君子用罔貞厲羝羊觸藩羸其角",
"三二三九七":"大壯卦，貞吉悔凶藩決不嬴壯于大輿之輹",
"三九七五八":"大壯卦，喪羊于易无悔",
"四七一一九":"大壯卦，羝羊觸藩不能退不能遂无攸利艱則吉",
"一五五ＯＯ":"晉卦，晉如摧如貞吉",
"一六二Ｏ五":"晉卦，晉如愁如貞吉受茲介福于其王母",
"一六九一Ｏ":"晉卦，眾允悔亡",
"三五二一五":"晉卦，晉如鼫鼠貞厲",
"四二二五六":"晉卦，悔亡失得勿恤往吉无不利",
"四九二九七":"晉卦，晉其角維用伐邑厲吉无咎",
"六四七八Ｏ":"明夷卦，明夷于飛垂其翼君子于行三日不食有攸往主人有言",
"六五四八五":"明夷卦，明夷于左股用拯馬壯吉",
"六六一九Ｏ":"明夷卦，明夷于南狩得其大首不可疾貞",
"三Ｏ二八七":"明夷卦，入于左腹獲明夷之心于出門庭",
"三七三二八":"明夷卦，箕子之明夷利貞",
"四四三六九":"明夷卦，不明晦初登于天後入于地",
"六七七二六":"家人卦，閑有家",
"六八四六三":"家人卦，遂在中饋貞吉",
"六九二ＯＯ":"家人卦，家人嗃嗃悔厲吉婦子嘻嘻終吉",
"三三一三七":"家人卦，富家大吉",
"四Ｏ四九八":"家人卦，王假有家勿恤吉",
"四七八五九":"家人卦，有孚威如吉",
"五三ＯＯ九":"睽卦，悔亡喪馬勿逐自復見惡人无咎",
"五三七四六":"睽卦，遇主于巷无咎",
"五四四八三":"睽卦，見輿曳其牛掣其人天且劓无初有終",
"三六八二Ｏ":"睽卦，睽孤遇元夫交孚厲无咎",
"四四一八一":"睽卦，悔亡厥宗噬膚往何咎",
"五一五四二":"睽卦，睽孤見豕負塗載鬼一車先張之弧後說之弧匪寇婚媾往遇雨則吉",
"五七七三八":"蹇卦，往蹇來譽",
"五八四四三":"蹇卦，王臣蹇蹇匪躬之故",
"五九一四八":"蹇卦，往蹇來反",
"二九五八一":"蹇卦，往蹇來連",
"三六六二二":"蹇卦，大蹇朋來",
"四三六六三":"蹇卦，往蹇來碩吉利見大人",
"Ｏ八四五三":"解卦，无咎",
"Ｏ九一五八":"解卦，田獲三狐得黃矢貞吉",
"Ｏ九八六三":"解卦，負且乘致寇至貞吝",
"三Ｏ九八四":"解卦，解而拇朋至斯孚",
"三八Ｏ二五":"解卦，君子維有解吉有孚于小人",
"四五Ｏ六六":"解卦，公用射隼于高墉之上獲之无不利",
"五一八五六":"損卦，已事遄往无咎酌損之",
"五二五七七":"損卦，利貞征凶弗損益之",
"五三二九八":"損卦，三人行則損一人一人行則得其友",
"三五二九九":"損卦，損其疾使遄有喜无咎",
"四二五ＯＯ":"損卦，或益之十朋之龜弗克違元吉",
"四九七Ｏ一":"損卦，弗損之益无咎貞吉利有攸往得臣无家",
"二三ｏ四八":"益卦，利用為大作元吉无咎",
"二三七六九":"益卦，或益之十朋之龜弗克違永貞吉王用亨于帝吉",
"二四四九Ｏ":"益卦，益之用凶事无咎有孚中行告公用圭",
"三二四一一":"益卦，中行告公從利用為依遷國",
"三九六一二":"益卦，有孚惠心勿問元吉有孚惠我德",
"四六八一三":"益卦，或益之勿擊之立心勿恆凶",
"四六六三八":"夬卦，壯于前趾往不勝為咎",
"四七三九一":"夬卦，惕號莫夜有戎勿恤",
"四八一四四":"夬卦，壯于頄有凶君子夬夬獨行遇雨若濡有慍无咎",
"三六一一三":"夬卦，臀无膚其行次且牽羊悔亡聞言不信",
"四三六三四":"夬卦，莧陸夬夬中行无咎",
"五一一五五":"夬卦，无號終有凶",
"四六一一六":"姤卦，繫于金柅貞吉有攸往見凶羸豕孚躅躑",
"三二三四八":"姤卦，包有魚不利賓",
"三三一Ｏ一":"姤卦，臀无膚其行次且厲无大咎",
"三五三五八":"姤卦，包无魚起凶",
"四二八七九":"姤卦，以杞包瓜含章有隕自天",
"五Ｏ四ＯＯ":"姤卦，姤其角吝无咎",
"一五四九八":"萃卦，有孚不終乃亂乃萃若號一握為咲勿恤往无咎",
"一六二Ｏ三":"萃卦，引吉无咎孚乃利用禴",
"一一九Ｏ八":"萃卦，萃如嗟如无攸利往无咎小吝",
"三三八Ｏ五":"萃卦，大吉无咎",
"四Ｏ八四六":"萃卦，萃有位无咎匪孚元永貞悔亡",
"四七八八七":"萃卦，齎咨涕洟无咎",
"二九五七五":"升卦，允升大吉",
"三Ｏ二八Ｏ":"升卦，孚乃利用禴无咎",
"三Ｏ九八五":"升卦，升虛邑",
"三Ｏ二八二":"升卦，王用享于岐山吉无咎",
"三七三二二":"升卦，貞吉升階",
"四四三六四":"升卦，冥升利于不息之貞",
"Ｏ八六四九":"困卦，臀困于株木入于幽谷三歲不覿",
"Ｏ九三七Ｏ":"困卦，困于酒食朱紱方來利用亨貞凶无咎",
"一ＯＯ九一":"困卦，困于石據于蒺蔾入于其宮不見其妻凶",
"三四五七二":"困卦，來徐徐困于金車吝有終",
"四一七七三":"困卦，劓刖困于赤紱乃徐有說利用祭祀",
"四八九七四":"困卦，困于葛藟于臲卼曰動悔有悔征吉",
"三Ｏ二四六":"井卦，井泥不食舊井无禽",
"三Ｏ九六七":"井卦，井谷射鮒甕敝漏",
"三一六八八":"井卦，井渫不食為我心惻可用汲王明並受其福",
"三Ｏ二四九":"井卦，井甃无咎",
"三七四五Ｏ":"井卦，井洌寒泉食",
"四四六五一":"井卦，井收勿幕有孚元吉",
"六七七二九":"革卦，鞏用黃牛之革",
"六八四六六":"革卦，已日乃革之征吉无咎",
"六九一Ｏ四":"革卦，征凶貞厲革言三就有孚",
"三五三四八":"革卦，悔亡有孚改命吉",
"四二七Ｏ九":"革卦，大人虎變未占有孚",
"五ＯＯ七Ｏ":"革卦，君子豹變小人革面征凶居貞吉",
"三Ｏ九二六":"鼎卦，鼎顛趾利出否得妾以其子无咎",
"三一六六三":"鼎卦，鼎有實我仇有疾不我能即吉",
"三二四ＯＯ":"鼎卦，鼎耳革其行塞雉膏不食方雨虧悔終吉",
"三六八一七":"鼎卦，鼎折足覆公餗其形渥凶",
"四四一七八":"鼎卦，鼎黃耳金鉉利貞",
"五一五三九":"鼎卦，鼎玉鉉大吉无不利",
"二二五三五":"震卦，震來虩虩后咲言啞啞吉",
"二三二四Ｏ":"震卦，震來厲億喪貝躋于九陵勿逐七日得",
"二三九四五":"震卦，震蘇蘇震行无眚",
"三Ｏ九八六":"震卦，震遂泥",
"三八Ｏ二七":"震卦，震往來厲億无喪有事",
"四五Ｏ六八":"震卦，震索索視矍矍征凶震不于其躬于其鄰无咎婚媾有言",
"五七七四五":"艮卦，艮其趾无咎利永貞",
"五八四五Ｏ":"艮卦，艮其腓不拯其隨其心不快",
"五九一五五":"艮卦，艮其限列其夤厲薰心",
"三四五一六":"艮卦，艮其身无咎",
"四一五五七":"艮卦，艮其輔言有序悔亡",
"四八五九八":"艮卦，敦艮吉",
"五九Ｏ二三":"漸卦，鴻漸于干小子厲有言无咎",
"五九七七四":"漸卦，鴻漸于磐飲食衎衎吉",
"六Ｏ四九五":"漸卦，鴻漸于陸夫征不復婦孕不有凶利禦寇",
"三二四一六":"漸卦，鴻漸于桷无咎",
"三九六一七":"漸卦，鴻漸于陵婦三歲不孕終莫之勝吉",
"四六八一八":"漸卦，鴻漸于陸其羽可用為儀吉",
"五一八五一":"歸妹卦，歸妹以娣跛能履征吉",
"五二五七二":"歸妹卦，眇能視利幽人貞吉",
"五三二五三":"歸妹卦，歸妹以須反歸以娣",
"三一六九四":"歸妹卦，歸妹愆期遲歸有時",
"三八八九五":"歸妹卦，帝乙歸妹其君之袂不如其子之袂",
"四六Ｏ九六":"歸妹卦，女承筐无實士刲羊无血",
"六六二五三":"豐起，遇其配主雖旬无咎往有尚",
"六六九七四":"豐起，豐其蔀日中見斗往得疑疾有孚發若吉",
"六七六九五":"豐起，豐其沛日中見沬折其右肱无咎",
"三一六九六":"豐起，豐其蔀日中見斗遇其夷主吉",
"三八八九七":"豐起，來章有慶譽吉",
"四六Ｏ九八":"豐起，豐其屋蔀其家闚其戶間其无人",
"五九Ｏ五八":"旅卦，旅瑣瑣斯其所取災",
"五九七七九":"旅卦，旅即次懷其資得童僕貞厲",
"六Ｏ五ＯＯ":"旅卦，旅焚其次喪其童僕貞厲",
"三六Ｏ二一":"旅卦，旅于處得其資斧我心不快",
"四三二二二":"旅卦，射雉一矢亡終以譽命",
"五Ｏ四二三":"旅卦，鳥焚其巢旅人先笑後號咷喪牛于易凶",
"三Ｏ九二一":"巽卦，進退利武人之貞",
"三一六五八":"巽卦，巽在牀下用史巫紛若吉无咎",
"三二三九五":"巽卦，頻巽吝",
"三三一三二":"巽卦，悔亡田獲三品",
"四Ｏ四九三":"巽卦，貞吉悔亡无不利无初有終先庚三日後庚三日吉",
"四七八五四":"巽卦，巽在牀下喪其資斧貞吉",
"五二ＯＯ七":"兌卦，和兌吉",
"五三七四四":"兌卦，孚兌吉悔亡",
"五四四八一":"兌卦，來兌凶",
"三五三四六":"兌卦，商兌未寧介疾有喜",
"四二七Ｏ七":"兌卦，孚于剝有厲",
"五ＯＯ六八":"兌卦，引兌",
"Ｏ八六四六":"渙卦，用拯馬壯吉",
"Ｏ九三六七":"渙卦，渙奔其機悔亡",
"一ＯＯ八八":"渙卦，渙其躬无悔",
"三二四Ｏ九":"渙卦，渙其群元吉渙有丘匪夷所思",
"三九六一Ｏ":"渙卦，渙汗其大號渙王居无咎",
"四六八一一":"渙卦，渙其血去逖出无咎",
"五一八四九":"節卦，不出戶庭无咎",
"五二五七Ｏ":"節卦，不出門庭凶",
"五三二九一":"節卦，不節若則嗟若无咎",
"三Ｏ二五二":"節卦，安節吉",
"三七四五三":"節卦，甘節吉往有尚",
"四四六五四":"節卦，苦節貞凶悔亡",
"五三ＯＯ四":"中孚卦，虞吉有它不燕",
"五三七四一":"中孚卦，鳴鶴在陰其子和之我有好爵吾與爾靡之",
"五四四七八":"中孚卦，得敵或鼓或罷或泣或歌",
"三三一三五":"中孚卦，月幾望馬匹亡无咎",
"四Ｏ四九六":"中孚卦，有孚攣如无咎",
"四七八五七":"中孚卦，翰音登于天貞凶",
"五七七四Ｏ":"小過卦，飛鳥以凶",
"五八四四五":"小過卦，過其祖遇其妣不及其君遇其臣无咎",
"五九一五Ｏ":"小過卦，弗過防之從或戕之凶",
"三Ｏ九九一":"小過卦，无咎弗過遇之往厲必戒勿用永貞",
"三八Ｏ三二":"小過卦，密雲不雨自我西郊公弋取彼在穴",
"四五Ｏ七三":"小過卦，弗遇過之飛鳥離之凶是謂災眚",
"六六一五一":"既濟卦，曳其輪濡其尾无咎",
"六六九七二":"既濟卦，婦喪其茀勿逐七日得",
"六七六九三":"既濟卦，高宗伐鬼方三年克之小人勿用",
"三Ｏ二五四":"既濟卦，繻有衣袽終日戒",
"三七四五五":"既濟卦，東鄰殺牛不如西鄰之禴祭實受其福",
"四四六五六":"既濟卦，濡其首厲",
"Ｏ八六五一":"未濟卦，濡其尾吝",
"Ｏ九三七二":"未濟卦，曳其輪貞吉",
"一ＯＯ九三":"未濟卦，未濟貞凶利涉大川",
"三六Ｏ一四":"未濟卦，貞吉悔亡震用伐鬼方三年有賞于大國",
"四二二一五":"未濟卦，貞吉悔亡君子之光有孚吉",
"五Ｏ四一六":"未濟卦，有孚于飲酒无咎濡其首有孚失是"}
