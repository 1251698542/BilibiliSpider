# bilibilispider

 ��ȡ[bilibili��վ](https://www.bilibili.com/)up�����и�����Ϣ��������Ƶ��Ϣ



## һ.Requirements������

```
python3
database:mongodb
module:requests,pymongo,BeautifulSoup,PyQuery
```



## ��.Description����

1. �����û�id���û��ǳƣ���ȡbilibili��վup���ĸ�����Ϣ����Ƶ��Ϣ,�����ص����ء�
   **����Bվ�û���������ȱ�ݣ��ǳƲ����п��ܳ���**��
2. ����Ŀ����Ҫ�߼���`spiders.py`�С�
3. ����Bվ�����۷���ȡ���ƽ�ǿ����ʹ�ô�������**���ų���BAN�Ŀ���**������رգ�ǰ��`config.py`�رա�
   ����ʹ�õ�����Ѵ�������ʱЧ�ϲ
   ������´���ǰ��`spiders.py`ִ��`Proxy_Spider`��
   ����������ʹ����ͨ����ǰ��`spiders.py`ִ��`Test_Spider`��
4. ֧�ִ洢���ָ�ʽ(�ɶ�ѡ):
  * json
  * csv
  * mongoDB



## ��.����Ŀ��ȡ����Ϣ

**������Ϣ**:

```
�ǳ�,�û�id,ͷ��
�Ա�,�ȼ�,����,ǩ��,����
��˿��,��ע��,��Ƶ�ܲ�����
������
�����Ƶ��Ϣ
```
**��Ƶ��Ϣ**:

```
����,����,��Ƶid,av��
ʱ��,��Ƶ���,��ǩ
Ӳ����,��Ļ��,�ղ���,������,������,�ۿ���,�Ƿ�ԭ��
��Ļ,����
```



## ��.download�ļ���:

```
proxies_info : �������ip
uploaders_img ������up����ͷ��ͼƬ
uploaders_info ������up���ĸ�����Ϣ
video_bulletscreen_info : ������Ƶ�ĵ�Ļ��Ϣ
video_img ��������Ƶ�ķ���
video_info ������up����������Ƶ��Ϣ
video_reply_info ��������Ƶ���ۣ��������򲻻ᱣ�棩
```



