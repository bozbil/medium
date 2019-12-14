<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Wingdings;
	panose-1:5 0 0 0 0 0 0 0 0 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:8.0pt;
	margin-left:0in;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
a:link, span.MsoHyperlink
	{color:blue;
	text-decoration:underline;}
a:visited, span.MsoHyperlinkFollowed
	{color:#954F72;
	text-decoration:underline;}
p
	{margin-right:0in;
	margin-left:0in;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;}
pre
	{mso-style-link:"HTML Preformatted Char";
	margin:0in;
	margin-bottom:.0001pt;
	font-size:10.0pt;
	font-family:"Courier New";}
span.HTMLPreformattedChar
	{mso-style-name:"HTML Preformatted Char";
	mso-style-link:"HTML Preformatted";
	font-family:"Courier New";}
.MsoChpDefault
	{font-family:"Calibri",sans-serif;}
.MsoPapDefault
	{margin-bottom:8.0pt;
	line-height:107%;}
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
-->
</style>

</head>

<body lang=EN-GB link=blue vlink="#954F72">

<div class=WordSection1>

<p class=MsoNormal><span lang=TR style='font-size:18.0pt;line-height:107%;
color:red'>MS-Word  kullanarak Jupyter Notebook'da karma&#351;&#305;k raporlar
haz&#305;rlama</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>Jupyter notebook kullan&#305;yorsan&#305;z, birçok
yönden harika özelliklerinin oldu&#287;unu zaten biliyorsunuz. Özellikle
Markdown seçene&#287;i yazd&#305;&#287;&#305;n&#305;z programlar&#305;
raporla&#351;t&#305;rman&#305;zda ve aç&#305;klama eklemenizde harikalar
yaratman&#305;z&#305; sa&#287;l&#305;yor.</span></p>

<p class=MsoNormal><span lang=TR><img width=601 height=94 id="Picture 1"
src="Jupyter_files/image001.jpg"></span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>Ancak Markdown k&#305;sm&#305;n&#305;n
baz&#305; zorluklar&#305; da yok de&#287;il. Örne&#287;in tablo eklemek. Tablo
eklemek basit manada kolay ancak, karma&#351;&#305;k tablolar ekleme i&#351;i
biraz “karma&#351;&#305;k”. Ben bu yaz&#305;mda bu i&#351;lem için ufak ama çok
etkili bir numara gösterece&#287;im. Üstelik bunu yaln&#305;zca tablolar için
de&#287;il, raporunuzdaki tüm karma&#351;&#305;k k&#305;s&#305;mlar için
kullanabilirsiniz (resim, video, link ekleme vs). Örne&#287;in, Bu yaz&#305;
bahsetti&#287;im yöntemle yaz&#305;larak, Github’a eklendi. A&#351;a&#287;&#305;daki
tablo ise tamamen alakas&#305;z, ancak olay&#305; biraz daha zor hale getirmek
için olu&#351;turuldu.</span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 align=left
 width=468 style='width:350.85pt;border-collapse:collapse;margin-left:6.75pt;
 margin-right:6.75pt'>
 <tr style='height:12.1pt'>
  <td width=198 colspan=3 style='width:148.15pt;border:solid windowtext 1.0pt;
  background:#00B050;padding:0in 5.4pt 0in 5.4pt;height:12.1pt'></td>
  <td width=66 style='width:49.4pt;border:solid windowtext 1.0pt;border-left:
  none;background:#00B050;padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal><span style='color:white'>De&#287;erler</span></p>
  </td>
  <td width=66 style='width:49.4pt;border:solid windowtext 1.0pt;border-left:
  none;background:#00B050;padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal><span style='color:white'>De&#287;erler</span></p>
  </td>
  <td width=70 style='width:52.8pt;border:solid windowtext 1.0pt;border-left:
  none;background:#00B050;padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal><span style='color:white'>De&#287;erler</span></p>
  </td>
  <td width=68 style='width:51.1pt;border:solid windowtext 1.0pt;border-left:
  none;background:#00B050;padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal><span style='color:white'>De&#287;erler</span></p>
  </td>
 </tr>
 <tr style='height:12.1pt'>
  <td width=68 rowspan=3 style='width:51.3pt;border:solid windowtext 1.0pt;
  border-top:none;background:#FFC000;padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal><span style='color:black'>Yöntem1 </span></p>
  </td>
  <td width=129 colspan=2 style='width:96.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal>Altyöntem1</p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal>1</p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal>1</p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal>1</p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal>1</p>
  </td>
 </tr>
 <tr style='height:12.6pt'>
  <td width=129 colspan=2 style='width:96.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:red'>Altyöntem2</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal>2</p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal>2</p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal>2</p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal>2</p>
  </td>
 </tr>
 <tr style='height:15.7pt'>
  <td width=129 colspan=2 style='width:96.85pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:15.7pt'>
  <p class=MsoNormal><span style='color:red'>Altyöntem3</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:15.7pt'>
  <p class=MsoNormal>3</p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:15.7pt'>
  <p class=MsoNormal>3</p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:15.7pt'>
  <p class=MsoNormal>3</p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:15.7pt'>
  <p class=MsoNormal>3</p>
  </td>
 </tr>
 <tr style='height:5.5pt'>
  <td width=68 rowspan=6 style='width:51.3pt;border:solid windowtext 1.0pt;
  border-top:none;background:#FFC000;padding:0in 5.4pt 0in 5.4pt;height:5.5pt'>
  <p class=MsoNormal><span style='color:black'>Yöntem2</span></p>
  </td>
  <td width=85 rowspan=2 style='width:63.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:5.5pt'>
  <p class=MsoNormal><span style='font-size:7.0pt;line-height:107%'>Altyöntem1</span></p>
  </td>
  <td width=44 style='width:33.35pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:5.5pt'>
  <p class=MsoNormal><span style='font-size:9.0pt;line-height:107%'>Yön1</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:5.5pt'>
  <p class=MsoNormal><u>4</u></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:5.5pt'>
  <p class=MsoNormal><u>4</u></p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:5.5pt'>
  <p class=MsoNormal><u>4</u></p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:5.5pt'>
  <p class=MsoNormal><u>5</u></p>
  </td>
 </tr>
 <tr style='height:12.1pt'>
  <td width=44 style='width:33.35pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.1pt'>
  <p class=MsoNormal><span style='font-size:9.0pt;line-height:107%'>Yön2</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal><s>5</s></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal><s>5</s></p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal><s>5</s></p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.1pt'>
  <p class=MsoNormal><s>6</s></p>
  </td>
 </tr>
 <tr style='height:12.6pt'>
  <td width=85 rowspan=2 style='width:63.5pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='font-size:7.0pt;line-height:107%'>Altyöntem2</span></p>
  </td>
  <td width=44 style='width:33.35pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='font-size:9.0pt;line-height:107%'>Yön1</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal><b>6</b></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal><b>6</b></p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal><b>6</b></p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:12.6pt'>
  <p class=MsoNormal><b>7</b></p>
  </td>
 </tr>
 <tr style='height:12.6pt'>
  <td width=44 style='width:33.35pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='font-size:9.0pt;line-height:107%'>Yön2</span></p>
  </td>
  <td width=66 style='width:49.4pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal>7</p>
  </td>
  <td width=66 style='width:49.4pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal>7</p>
  </td>
  <td width=70 style='width:52.8pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal>7</p>
  </td>
  <td width=68 style='width:51.1pt;border:none;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal>8</p>
  </td>
 </tr>
 <tr style='height:12.6pt'>
  <td width=129 colspan=2 rowspan=2 style='width:96.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#92D050;padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>Altyöntem3</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>8</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>8</span></p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>8</span></p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>8</span></p>
  </td>
 </tr>
 <tr style='height:12.6pt'>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>9</span></p>
  </td>
  <td width=66 style='width:49.4pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>9</span></p>
  </td>
  <td width=70 style='width:52.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>9</span></p>
  </td>
  <td width=68 style='width:51.1pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:#92D050;
  padding:0in 5.4pt 0in 5.4pt;height:12.6pt'>
  <p class=MsoNormal><span style='color:black'>9</span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>Bu i&#351;lem için tek ihtiyac&#305;m&#305;z
olan &#351;ey bir kelime i&#351;lemci program&#305;. Ben MS Word
kullan&#305;yorum. Kelime i&#351;lemcinizde raporunuzu olu&#351;turun ve
kaydedin. Daha sonra bu raporu File (dosya)</span><span lang=TR
style='font-family:Wingdings'>à</span><span lang=TR> Save as (farkl&#305;
kaydet) seçene&#287;ini kullanarak “Web Page, Filtered (*.htm, *.html)” ( Web
Sayfas&#305;, filtrelenmi&#351; htm) olarak kaydedin. </span></p>

<p class=MsoNormal><span lang=TR><img width=474 height=268 id="Picture 2"
src="Jupyter_files/image002.jpg"></span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>A&#351;a&#287;&#305;da gördü&#287;ünüz gibi
dosya olu&#351;turuldu. E&#287;er dosya içerisinde resim vs gibi ekler
kulland&#305;ysan&#305;z, dosyan&#305;z&#305;n yan&#305;nda, bu eklerin
tutuldu&#287;u bir klasör de yarat&#305;lacakt&#305;r(dosyaismi_files).</span></p>

<p class=MsoNormal><img width=313 height=215 id="Picture 3"
src="Jupyter_files/image003.png"></p>

<p class=MsoNormal><span lang=TR>&#350;imdi tek yapman&#305;z gereken
olu&#351;turulan dosyay&#305; bir metin editörü (notdefteri-notepad, notepad++
vs ) kullanarak açmak içerisindeki html kodunu kopyalay&#305;p jupyter notebook
hücresine  yap&#305;&#351;t&#305;rmak. </span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR><br>
</span><img width=551 height=265 id="Picture 4" src="Jupyter_files/image004.jpg"></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR><img width=601 height=358 id="Picture 5"
src="Jupyter_files/image005.jpg"></span></p>

<p class=MsoNormal><span lang=TR>Hücrenin Markdown modunda olmas&#305;na dikkat
edin ve ek klasörü de dosyan&#305;n yan&#305;na ta&#351;&#305;may&#305;
unutmay&#305;n. Aksi takdirde, ekledi&#287;iniz resimler görülmeyecektir</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR><br>
<br>
<br>
</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;background:white;vertical-align:baseline'><span style='font-size:12.0pt;
color:black'>&nbsp;</span></p>

<p class=MsoNormal><span lang=TR>&nbsp;</span></p>

</div>

</body>

</html>
