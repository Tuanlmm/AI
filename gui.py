import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy as np
# load the trained model to classify sign
from keras.models import load_model
model = load_model('model2.h5')

# dictionary to label all traffic signs class.
classes = {1: 'Giới hạn tốc độ (20km/h)',
           2: 'Giới hạn tốc độ (30km/h)',
           3: 'Giới hạn tốc độ (50km/h)',
           4: 'Giới hạn tốc độ (60km/h)',
           5: 'Giới hạn tốc độ (70km/h)',
           6: 'Giới hạn tốc độ (80km/h)',
           7: 'Kết thúc giới hạn tốc độ (80km/h)',
           8: 'Giới hạn tốc độ (100km/h)',
           9: 'Giới hạn tốc độ (120km/h)',
           10: 'Cấm vượt',
           11: 'Cấm vượt xe > 3.5 tấn',
           12: 'Ưu tiên tại ngã ba, ngã tư',
           13: 'Đường ưu tiên',
           14: 'Nhường đường',
           15: 'Stop (Dừng)',
           16: 'Cấm xe cơ giới',
           17: 'Cấm xe cơ giới > 3.5 tấn',
           18: 'Cấm đi',
           19: 'Chú ý phía trước',
           20: 'Chỗ ngoặt nguy hiểm bên trái',
           21: 'Chỗ ngoặt nguy hiểm bên phải',
           22: 'Chỗ ngoặt kép',
           23: 'Đường xấu',
           24: 'Đường trơn trượt',
           25: 'Đường thu hẹp bên phải',
           26: 'Công trường đang làm việc',
           27: 'Đèn tín hiệu giao thông',
           28: 'Người đi bộ',
           29: 'Chỗ qua đường cho trẻ em',
           30: 'Chỗ qua đường cho xe đạp',
           31: 'Chú ý đường băng/tuyết',
           32: 'Băng qua đường có vật nuôi hoang dã',
           33: 'Kết thúc giới hạn tốc độ + cấm vượt',
           34: 'Rẽ phải phía trước',
           35: 'Rẽ trái phía trước',
           36: 'Chỉ đi thẳng',
           37: 'Chỉ đi thẳng hoặc rẽ phải',
           38: 'Chỉ đi thẳng hoặc rẽ trái',
           39: 'Luôn giữ bên phải',
           40: 'Luôn giữ bên trái',
           41: 'Luồng xe đi vòng xuyến bắt buộc',
           42: 'Kết thúc cấm vượt',
           43: 'Kết thúc cấm vượt xe > 3.5 tấn'}


def classify(file_path):
    try:
        image = Image.open(file_path)
        image = image.resize((30, 30))
        image = image.convert('RGB')
        image = np.array(image)
        image = np.expand_dims(image, axis=0)  # Thêm chiều cho batch size
        predictions = model.predict(image)
        predicted_class = np.argmax(predictions[0]) + 1
        sign = classes[predicted_class]
        return sign
    except Exception as e:
        print(e)
        return "Error predicting"


def show_image(file_path):
    img = Image.open(file_path)
    img.thumbnail((200, 200))
    photo = ImageTk.PhotoImage(img)
    return photo


def display_prediction(file_path):
    result = classify(file_path)
    image = show_image(file_path)

    # Hiển thị hình ảnh gốc
    original_img_label.config(image=image)
    original_img_label.image = image

    # Hiển thị hình ảnh đã được dự đoán
    predicted_img_label.config(
        text=f"Predicted: {result}", font=('Arial', 16), fg='green')


def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_prediction(file_path)


root = tk.Tk()
root.title("Nhan dien bien bao")
root.geometry("600x400")
root.configure(background='#f0f0f0')

label_nhom_18 = tk.Label(root, text="Nhom 18", font=("Arial", 14))
label_nhom_18.pack(side=tk.BOTTOM, pady=10)

upload_button = Button(root, text="Upload Image", command=upload_image, font=(
    'Arial', 12), bg='#4CAF50', fg='white')
upload_button.pack(pady=20)

img_frame = Frame(root, bg='#f0f0f0')
img_frame.pack(pady=20)

original_img_label = Label(img_frame)
original_img_label.grid(row=0, column=0, padx=10)

predicted_img_label = Label(
    img_frame, text="No Prediction", font=('Arial', 16), bg='#f0f0f0')
predicted_img_label.grid(row=0, column=1, padx=10)

root.mainloop()
