import streamlit as st
import pandas as pd
import plotly.express as px

def thongkesudung():
    st.header("Thống kê ra vào 2")
                #Load data
    list_chart=["","Biểu đồ đường","Biểu đồ cột","Xuất file Excel"]
    selected=st.selectbox("Hãy chọn biểu đồ cần hiển thị",list_chart)
    if(selected==""):
        st.info("Hãy chọn biểu đồ trước")
    elif selected=="Biểu đồ đường":

        excel_file='src/detection_count.csv'
        sheet_name="Count Detection"
        coulumn=['Thời gian','Số người']
        df=pd.read_csv(excel_file,names=coulumn,sep=",")
        df['Thời gian'] = pd.to_datetime(df['Thời gian'])

        # Thiết lập cột "Thời gian" làm chỉ mục (index)
        df.set_index('Thời gian', inplace=True)

        # Hiển thị DataFrame
        st.write('Dữ liệu ban đầu:')
        st.write(df)

        # Vẽ đồ thị bằng Plotly
        fig = px.line(df, title='Biểu đồ Số người theo thời gian')
        st.plotly_chart(fig, use_container_width=True)


    elif selected=="Biểu đồ cột":
        excel_file = 'src/detection_count.csv'
        sheet_name = "Count Detection"
        coulumn = ['Thời gian', 'Số người']
        df = pd.read_csv(excel_file, names=coulumn, sep=",")
        df['Thời gian'] = pd.to_datetime(df['Thời gian'])

        # Thiết lập cột "Thời gian" làm chỉ mục (index)
        df.set_index('Thời gian', inplace=True)
        #st.area_chart(df)
        st.bar_chart(df)
    elif selected=="Xuất file Excel":
        import os
        import glob
        import csv
        from xlsxwriter.workbook import Workbook

        for csvfile in glob.glob('src/detection_count.csv'):
            workbook = Workbook(csvfile[:-4] + '.xlsx')
            worksheet = workbook.add_worksheet()
            with open(csvfile, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()


        with open("src/detection_count.xlsx", "rb") as file:
            btn = st.download_button(
                label="Download file as Excel File",
                data=file,
                file_name="Detection_Count.xlsx",
            )

