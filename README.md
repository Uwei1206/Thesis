# Thesis
## 應用深度學習於肺部疾病的輔助鑑別診斷之研究 
[論文連結](https://hdl.handle.net/11296/4p3z7a) ，電子全文網際網路公開日期：20270624

### 摘要
近年來，隨著台灣目前各項科技技術的進步與發展，人工智能對研究解決不同領域挑戰的方式產生顯著的影響，尤其是在醫療領域。由於嚴重特殊傳染性肺炎的發生，讓肺炎又受到了高度的關注。據我國衛生福利部的調查，國人死因統計當中，肺炎位居前三，而肺癌更是癌症死亡率之首。導致肺部疾病的成因很多，菸害與空氣汙染更是佔了不少比例，因此早期發現與治療成為了存活的關鍵，而胸部X光檢查是肺部疾病檢查最常見的診斷方法，但X光圖像需要經過培訓的放射科醫生來解釋，目前因為疫情的爆發，平日大量的影像也使醫事放射師和放射科醫師的工作負擔大幅增加，造成我國檢驗量能不足的現象，此外，在解釋時也可能因為各種因素導致結果誤判，因此需要一個可靠的解決方案。
### 數據來源
[數據整理網址](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

本研究以阿拉伯的卡達大學(Qatar University)及位於孟加拉的達卡大學(University of Dhaka)的研究團隊與巴基斯坦和馬來西亞的醫生及合作者所共同創建的醫療圖像數據庫實施研究。
該圖像類別包含四類：
- COVID-19 (嚴重特殊傳染性肺炎)
- Normal (正常)
- Lung Opacity (肺部渾濁)
- Viral Pneumonia (病毒性肺炎)
### 研究方法
- 模型
  1. CNN
  2. CNN+SVM
- 驗證與評估方法
  1. 混淆矩陣(confusion matrix)
  2. Roc曲線(ROC Curve)
  3. Kappa係數
  4. 成對樣本T檢定
  5. K-Fold 

利用卷積神經網路對醫療影像建構分類模型，透過卷積神經網路自動提取特徵的能力，以及良好的分類性能對四種類別的圖像進行分類，除了原始的卷積神經網路外，在輸出分類影像時，將卷積神經網路的分類替換為結合支援向量機，建構兩種分類模型並以交叉驗證、混淆矩陣、ROC曲線與Kappa係數對模型進行各項驗證與評估。
### 研究結果
研究結果顯示，透過成對樣本T檢定得知分類模型之間的準確率與ROC曲線下面積皆無顯著差異，透過交叉驗證兩模型的平均準確率皆高於87%以上，平均ROC曲線下面積也高達0.97以上，具備良好的分類性能，此外，兩模型的Kappa係數值也高於0.82，具備良好的一致性，可供醫師作為輔助診斷之工具及參考。
