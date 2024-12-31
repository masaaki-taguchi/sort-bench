# デフォルトサフィックスを削除
.SUFFIXES:

# 各種コマンド短縮名
RUN68 = run68
BASE_DIR = /Users/masaaki/x68000/HFS/develop
AS = $(RUN68) ${BASE_DIR}/bin/HAS.X
LK = $(RUN68) ${BASE_DIR}/bin/HLK.X

# プログラム名(拡張子除く)
PROG = ../SORT

# ヘッダ検索パス
INCLUDE_FLAGS = -I${BASE_DIR}/include/xc

# *.HAS ソースファイル
ASM_SRCS = SORT.HAS

# 中間ファイル生成用ディレクトリ
INTERMEDIATE_DIR = _build

# オブジェクトファイル
OBJS =	$(addprefix $(INTERMEDIATE_DIR)/,$(patsubst %.HAS,%.o,$(ASM_SRCS)))

# HLK に入力するリンクリスト
HLK_LINK_LIST = $(INTERMEDIATE_DIR)/_lk_list.tmp

# デフォルトのターゲット
all : $(PROG).FNC

# 中間生成物の削除
clean : 
	rm -f $(PROG).FNC
	rm -rf $(INTERMEDIATE_DIR)

# 実行ファイルの生成
#	HLK に長いパス文字を与えることは難しい。
#	回避策としてリンク対象ファイルを $(INTERMEDIATE_DIR) 以下にコピーし、
#	短い相対パスを用いてリンクを実行させる。
$(PROG).FNC : $(OBJS)
	mkdir -p $(INTERMEDIATE_DIR)
	rm -f $(HLK_LINK_LIST)
	@for FILENAME in $(OBJS); do\
		echo $$FILENAME >> $(HLK_LINK_LIST); \
        done
	$(LK) -i $(HLK_LINK_LIST) -o $(PROG).FNC

# *.HAS ソースのアセンブル
$(INTERMEDIATE_DIR)/%.o : %.HAS Makefile
	mkdir -p $(INTERMEDIATE_DIR)
	$(AS) -e -u -w0 $(INCLUDE_FLAGS) $*.HAS -o $(INTERMEDIATE_DIR)/$*.o

$(INTERMEDIATE_DIR)/SORT.o:	SORT.HAS
