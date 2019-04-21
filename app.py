# -*- coding:utf-8 -*-

from flask import Flask, jsonify, render_template, request, url_for
import jieba
import time
import threading
jieba.load_userdict("/Users/yanwei/www/mywork/python/participle/templates/dict.txt")

app = Flask(__name__)

app.secret_key = 'lening'


def fun_timer():
    jieba.load_userdict("/Users/yanwei/www/mywork/python/participle/templates/dict.txt")
    global timer
    timer=threading.Timer(1,fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()

#显示index.html页面方法
@app.route('/', methods=['get', 'post'])
def index():
    # url_for('static', filename='jquery-3.3.1.js')
    return render_template('index.html')

#处理添加到分词库方法
@app.route('/flask/add', methods=['post'])
def add():
    data = ''
    if request.method == 'POST':
        data = request.form["str"]
        fh = open('/Users/yanwei/www/mywork/python/participle/templates/dict.txt', 'a', encoding='utf-8')
        fh.write(data + "\n")
        fh.close()
        return 'success'


#处理文本内容进行结巴分词的方法
@app.route('/flask/fc', methods=['post'])
def fc():
    if request.method == 'POST':
        # 获取请求参数
        text1 = request.form["str"]
        text2 = jieba._lcut(text1)
        return jsonify(text2)


if __name__ == '__main__':
    app.run(debug=True)

