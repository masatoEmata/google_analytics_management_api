■概要
Googleアナリティクスの設定を一括取得・更新するためのスクリプト

■操作の流れ
(1)事前準備
  以下ドキュメントに沿って準備する
  https://developers.google.com/analytics/devguides/config/mgmt/v3/quickstart/service-py

  1.認証キーの取得
    ●GCPのサービスアカウントから認証設定でJSONキーを取得する
     ※参照「ステップ 1: アナリティクス API を有効にする」

    ●以下ディレクトリ内に設置する
      common > secret

  2.ライブラリの取得
    ●以下を実行
    $sudo pip install --upgrade google-api-python-client
      ※参照「ステップ 2: Google クライアント ライブラリをインストールする」

  3. Googleアナリティクスの権限にサービスアカウントを追加する)。

(2)データファイルの準備
  ●設定を取得する場合  
    methods > list_XXX.csvにヘッダー以外のデータがあれば削除
  ●設定を更新する場合 
    methods > input_file > update_XXX.csvにヘッダー付きのデータファイルを作成
    
(3)スクリプトの実行 
  ●「methods」フォルダの中にある以下ファイルを実行
  ・insertXXX.py ・・・ XXXを一括登録
  ・listXXX.py ・・・ XXXを一括取得
  ・updateXXX.py ・・・ XXXを一括更新

  ※中には以下のように実行しなければならないファイルがあるが、もし引数が足りずエラーが起こればその旨が表示される
  $ XXX.py <アカウントID> <プロファイルID>
