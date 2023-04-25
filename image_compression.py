{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8c0dcd5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "67643cf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_imgage(img):\n",
    "    image = np.load(img)\n",
    "    return image\n",
    "\n",
    "def compression(img, n):\n",
    "    image = plt.imread(img) \n",
    "    image = image[:,:,0]  \n",
    "    U, sing_vals, V = np.linalg.svd(image)\n",
    "    sigma = np.zeros(shape=(U.shape[0], V.shape[0]))\n",
    "    np.fill_diagonal(sigma, sing_vals)\n",
    "    trunc_U = U[:,:n]\n",
    "    trunc_sigma = sigma[:n,:n]\n",
    "    trunc_V = V[:n,:]\n",
    "    trunc_img = trunc_U@trunc_sigma@trunc_V\n",
    "    return plt.imshow(trunc_img)\n",
    "\n",
    "st.title('Сжатие изображений с использованием SVD')\n",
    "\n",
    "uploaded_img = st.file_uploader('Загрузите изображение', type=['png', 'jpeg', 'jpg'])\n",
    "if uploaded_img:\n",
    "    image = load_image(uploaded_img)\n",
    "    st.image(image, caption='Исходное изображение', use_column_width=True)\n",
    "    \n",
    "    n = st.slider('Количество сингулярных чисел', min_value=1, max_value=min(image.size), value=min(image.size)//2+1)\n",
    "\n",
    "    compressed_image = compression(image, n)\n",
    "    st.image(compressed_image, caption='Сжатое изображение', use_column_width=True)\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
