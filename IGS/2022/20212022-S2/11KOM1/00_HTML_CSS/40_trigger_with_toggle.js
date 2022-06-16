<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Click Box</title>
  </head>
  <style media="screen">
    .container {
      display: flex;
      justify-content: center;
    }

    .box {
      margin-top: 8rem;
      width: 10rem;
      height: 10rem;
      background: red;
    }

    div.box.clicked {
      transform: rotate(230deg);
      transition: 3s linear;
    }

  </style>
  <script type="text/javascript">
    // const clickedBox = function () {
    //   // console.log("clicked!")
    //   document.querySelector(".box").classList.add("clicked");
    // }

    document.addEventListener('DOMContentLoaded', () => {
      // document.querySelector(".box").onclick = function (){
      //   this.classList.add("clicked");
      // }

      document.querySelector(".box").addEventListener('click', function(){
        this.classList.add("clicked");
      })


    })
  </script>
  <body>
    <div class="container">
      <!-- onclick="clickedBox()" -->
      <div class="box"></div>
    </div>
  </body>
</html>
