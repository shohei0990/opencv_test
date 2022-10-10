import cv2
import streamlit as st

img = cv2.imread('res.jpg')
cv2.imwrite('res.jpg', img)

# ---------------------------------------------
# 画像色処理
res1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # グレースケール
res2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # HSV 明るさ・鮮やかさ
res3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR ⇒ RGB

st.title('CV2確認')
st.image( res1, caption='res1', use_column_width=True )
st.image( res2, caption='res2', use_column_width=True )
st.image( res3, caption='res3', use_column_width=True )

#cv2.imwrite('res1.jpg', res1)
#cv2.imwrite('res2.jpg', res2)
#cv2.imwrite('res3.jpg', res3)
# ---------------------------------------------