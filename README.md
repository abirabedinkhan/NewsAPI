
# NewsAPI

NewsAPI is a simple, easy-to-use REST API that returns JSON search results for current and historic news articles published by [Samakal](https://samakal.com/), [Politico](https://politico.com/)


## Installation

Install NewsAPI with pip3

```bash
  cd my-project
  pip3 install -r requirements.txt
  flask run
```
    
## Documentation

After running your server at http://127.0.0.1:5000/

### Input
```
  /politico?q={value}
```
### Output
```
[
    {
        "snippet": "Elections Article",
        "thumbnail": "https://static.politico.com/36/a2/461651fd471694b4167886e5a7d4/191112-miami-ap-773.jpg",
        "title": "\nPriorities USA launches Latino persuasion program in Florida",
        "url": "https://www.politico.com/news/2019/11/13/priorities-usa-launches-latino-persuasion-program-in-florida-070397"
    },
    {
        "snippet": "Blog Post",
        "thumbnail": "https://static.politico.com/65/c5/3c23e11c4fadbe96c4ebd8aaf26f/politico.png",
        "title": "\nUSA Today plans countrywide expansion",
        "url": "https://www.politico.com/blogs/media/2013/12/usa-today-plans-countrywide-expansion-179714"
    },
    {
        "snippet": "Elections Article",
        "thumbnail": "https://static.politico.com/ff/fd/589fc7644af781ea5096fdf0cae0/200608-phoenix-ap-773.jpg",
        "title": "\nPriorities USA expands TV ads in Arizona",
        "url": "https://www.politico.com/news/2020/06/09/arizona-democratic-super-pac-308126"
    },
    {
        "snippet": "Elections Article",
        "thumbnail": "https://static.politico.com/18/3d/215ea6884ea3ad2d1be8f3bda438/20200804-bass-gty-773.jpg",
        "title": "\nKaren Bass eulogized Communist Party USA leader",
        "url": "https://www.politico.com/news/2020/08/04/karen-bass-eulogized-communist-party-usa-leader-391455"
    }
]
```
### Input
```
  /samakal?q={value}
```
### Output
```
[
    {
        "snippet": "﻿অস্ট্রেলিয়াকে টানা দ্বিতীয়বার হারিয়ে সিরিজ জয়ের দৌড়ে এগিয়ে গেছে বাংলাদেশ। এই অর্জনে বাংলাদেশ দলকে আন্তরিক অভিনন্দন জানিয়েছেন প্রধানমন্ত্রী শেখ হাসিনা।বুধবার রাতে এক অভিনন্দন বার্তায় ক্রিকেট অনুরাগী প্রধানমন্ত্রী সব খেলোয়াড় কোচ ...",
        "thumbnail": "https://samakal.com/uploads/2021/08/online/thumbnails/a-samakal-610ab734bffbf.jpg",
        "title": "বাংলাদেশ দলকে অভিনন্দন জানালেন প্রধানমন্ত্রী",
        "url": "https://samakal.com/bangladesh/article/210872025/বাংলাদেশ-দলকে-অভিনন্দন-জানালেন-প্রধানমন্ত্রী"
    },
    {
        "snippet": "লন্ডনে ২৩ বছর আগে ৩২ বছরের এক নারীকে ধর্ষণ করেছিলেন বাংলাদেশি এক যুবক। এর দায়ে সেই গুলজার হোসাইনকে ১১ বছরের কারাদণ্ড দেওয়া হয়েছে। সম্প্রতি স্নেয়ার্সব্রুক ক্রাউন আদালতের বিচারক এ দণ্ড ...",
        "thumbnail": "https://samakal.com/uploads/2021/08/online/thumbnails/a-samakal-610a9fbc65e01.jpg",
        "title": "লন্ডনে ২৩ বছর আগে করা ধর্ষণের দায়ে বাংলাদেশির কারাদণ্ড",
        "url": "https://samakal.com/international/article/210871998/লন্ডনে-২৩-বছর-আগে-করা-ধর্ষণের-দায়ে-বাংলাদেশির-কারাদণ্ড"
    },
    {
        "snippet": "বাংলাদেশ এশিয়ার দ্রুত-বর্ধনশীল অর্থনীতির দেশ। বিনিয়োগের আকর্ষণীয় গন্তব্য। স্বাধীনতার সুবর্ণজয়ন্তীতে উন্নয়নের সিঁড়ি ধরে শেয়ারবাজারেও তৈরি হয়েছে অপার সম্ভাবনা। বৈশ্বিক আর্থিক প্রতিষ্ঠান এইচএসবিসির এক প্রতিবেদনে বাংলাদেশের অর্থনীতি নিয়ে এমন প্রশংসা করা ...",
        "thumbnail": "https://samakal.com/uploads/2021/08/online/thumbnails/Image_HSBC7-samakal-610a9757184d6.jpg",
        "title": "বিনিয়োগের আকর্ষণীয় গন্তব্য বাংলাদেশ",
        "url": "https://samakal.com/economics/article/210871992/বিনিয়োগের-আকর্ষণীয়-গন্তব্য-বাংলাদেশ-এইচএসবিসি"
    },
    {
        "snippet": "﻿দ্বিতীয় টি-টোয়েন্টিতে বাংলাদেশকে ১২২ রানের টার্গেট দিয়েছে অস্ট্রেলিয়া। আজ জিতলেই বাংলাদেশ ২-০ ব্যবধানে এগিয়ে যাবে।মিরপুরে আজ সিরিজের&nbsp;দ্বিতীয় টি-টোয়েন্টি ম্যাচে টস হেরেছে বাংলাদেশ। টস জিতে ব্যাটিংয়ের সিদ্ধান্ত নিয়েছেন অজি অধিনায়ক ম্যাথু ...",
        "thumbnail": "https://samakal.com/uploads/2021/08/online/thumbnails/167A2532-samakal-610a84d2c68f5.JPG",
        "title": "বাংলাদেশের টার্গেট ১২২",
        "url": "https://samakal.com/sports/article/210871973/অপরিবর্তিত-একাদশ-নিয়ে-ফিল্ডিংয়ে-বাংলাদেশ"
    }
]
```



  
## Authors

- [@AbirAbedinKhan](https://www.github.com/AbirAbedinKhan)

## License

[MIT](https://choosealicense.com/licenses/mit/)

  
