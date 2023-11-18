import align_dataset_mtcnn
import sys
import classifier

dataset_raw=r"D:\Facenet+Mtcnn_Project\Facenet+Mtcnn_Project\Dataset\FaceData\raw"
dataset_processed=r"D:\Facenet+Mtcnn_Project\Facenet+Mtcnn_Project\Dataset\FaceData\processed"
choose=int(input("Nhap lua chon: "))
if(choose==1):
    args = ['src/align_dataset_mtcnn.py', dataset_raw, dataset_processed, '--image_size', '160', '--margin', '32', '--random_order', '--gpu_memory_fraction', '0.25']
    align_dataset_mtcnn.main(align_dataset_mtcnn.parse_arguments(args[1:]))
if(choose==2):
# Train model với ảnh
    sys.argv = [r'D:\Facenet+Mtcnn_Project\Facenet+Mtcnn_Project\src\classifier.py', 'TRAIN', r'D:\Facenet+Mtcnn_Project\Facenet+Mtcnn_Project\Dataset\FaceData\processed', r'D:\Facenet+Mtcnn_Project\Facenet+Mtcnn_Project\Models\20180402-114759.pb', r'D:\Facenet+Mtcnn_Project\Facenet+Mtcnn_Project\Models\facemodel.pkl', "--use_split_dataset",'--batch_size', "1000"]
    classifier.main(classifier.parse_arguments(sys.argv[1:]))

