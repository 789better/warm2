# coding=utf8
import codecs
import random



i = 1;
select_text = ['789BIT เว็ปตรง เว็ปแท้ จ่ายครบ 100 เต็ม','789BIT เว็ปตรง เว็ปแท้ จ่ายเต็มทุกยอด', '789BIT สมัครสมาชิก เล่นเว็บตรงระบบ AUTO', '789BIT บริการ 24 ชั่วโมง สล็อค บอล หวย บาคาร่า คาสิโนออนไลน์', '789BIT แจกเครดิตฟรี กิจกรรมร่วมสนุกทุกสัปดาห์ไม่มีเงื่อนไข']
select_image = ['https://789bt-four.com/bit/1.jpg','https://789bt-four.com/bit/2.jpg','https://789bt-four.com/bit/3.jpg','https://789bt-four.com/bit/4.jpg','https://789bt-four.com/bit/5.jpg',
'https://789bt-four.com/bit/6.jpg','https://789bt-four.com/bit/7.jpg','https://789bt-four.com/bit/8.jpg','https://789bt-four.com/bit/9.jpg','https://789bt-four.com/bit/10.jpg','https://789bt-four.com/bit/11.jpg']



while i<10:
	html_str = '''
<head>
  <title>789BT เว็ปตรง แตกหนัก จ่ายจริง</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="789BT กิจกรรมมากมายแจกเครดิตฟรีทุกวัน ทายเลขท้าย 2 ตัวรับฟรี">
  <meta name="keywords" content="เสี่ยงโชค,หมุนวงล้อ,รับเครดิตฟรี">
  <link rel="stylesheet" href="https://789better.github.io/aff-ref/style.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <meta property="og:type"               content="article" />
  <meta property="og:title"              content="'''+str(random.choice(select_text))+'''" />
  <meta property="og:description"        content="ชวนเพื่อนรับเครดิตฟรี สูงสุด 5,000" />
  <meta property="og:image"              content="'''+str(random.choice(select_image))+'''?a=5" />
  <!-- Meta Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '1788950101506285');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=1788950101506285&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
  </head>
  <body>
  <div id="app" ></div>
  <div class="card" style="max-width:600px;margin:auto;">
    <div id = "section1">
  
      <div id = "jumbotron" class = "jumbotron" style="margin-top:20px;">
      <a href="https://aff.789bi.app/aff/4137427sz/facebook"><button class="button button2 blink" style="margin:20px 0px;background-color:red;font-size:2.5em;">สมัครสมาชิกใหม่</button></a>
        <div id="img_profile" ><img id="img_profile" width="80%" style="border-radius:15px;" src="'''+random.choice(select_image)+'''" alt="789BT"></div>
        <a href="https://aff.789bi.app/aff/4137427sz/facebook"><button class="button button2">สมัครสมาชิก</button></a>
        <a href="https://aff.789bi.app/aff/4137427sz/facebook"><button class="button button2">สมัครสมาชิก (ลิงค์สำรอง)</button></a>
        <p style="margin-bottom:0px;margin-top:5px;">@789BT เว็ปดี มีทุกเกมส์</p>
      </div>  
  
    </div>
    </div>
  </body>
'''
	Html_file= codecs.open(str(i)+".html","w", "utf-8")
	Html_file.write(html_str)
	Html_file.close()
	i += 1