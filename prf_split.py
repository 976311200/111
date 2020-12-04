#!/usr/bin/env python
# coding=utf-8

from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf(start_page, end_page, pdf_dir, save_dir):
    print(save_dir)
    start_page = start_page -1
    end_page = end_page

    fp_read_file = open(pdf_dir, 'rb')
    pdf_input = PdfFileReader(fp_read_file,strict=False)  # 将要分割的PDF内容格式话
    page_count = pdf_input.getNumPages()  # 获取PDF页数
    print("该文件共有{}页".format(page_count))  # 打印页数
    pdf_name = pdf_dir.split('/')[-1].split('.')[0]
    name = pdf_name

    pdf_file = str(save_dir)+"/" + str(start_page)+ '-' + str(end_page) + name + '.pdf'
    print(pdf_file)
    try:
        print(f'开始分割{start_page+1}页-{end_page}页，保存为{pdf_file}......')
        pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器
        for i in range(start_page, end_page):
            pdf_output.addPage(pdf_input.getPage(i))
        with open(pdf_file, 'wb') as sub_fp:
            pdf_output.write(sub_fp)
        print(f'完成分割{start_page+1}页-{end_page}页，保存为{pdf_file}!') 
    except IndexError:
        print(f'分割页数超过了PDF的页数')



