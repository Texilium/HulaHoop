
<template>
  <div id="app" >
    {{ /*START HEADER */ }}
    <div>
      <b-navbar id="navbar_" ref="navbar_" toggleable="lg" type="dark" variant="danger" >
        <span id="coin_cont" href="#"> <img src="logo.png" id="coin"/></span>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" class="container" is-nav >
          <b-navbar-nav>
              <h4 class="header_title">Sezioni</h4>
              <span id="header_pages_cont" >
                <button id="home_btn" class="header_btn" v-on:click="(e)=>{this.target_page='Home'}">Home</button>
                <button id="servizi_btn" class="header_btn"  v-on:click="(e)=>{this.target_page='Servizi'}">Servizi</button>
                <button id="eventi_btn" class="header_btn" v-on:click="(e)=>{this.target_page='Eventi'}">Eventi</button>
                <button id="prodotti_btn" class="header_btn" v-on:click="(e)=>{this.target_page='Prodotti'}">Prodotti</button>
                <button id="preferiti_btn" class="header_btn" v-on:click="(e)=>{this.target_page='Preferiti'}">Preferiti</button>
                <button  ref="header_btn" id="team_btn" class="header_btn" v-on:click="(e)=>{this.target_page='Team'}">Team</button>
                <button id="contatti_btn" class="header_btn" v-on:click="(e)=>{this.target_page='Contatti'}">Contatti</button>


              </span>  
              
              <div id="header_social_cont">
                <b-nav-item href="https://www.instagram.com" target="_blank"><font-awesome-icon :icon="`fa-brands fa-instagram`"/></b-nav-item>
                <b-nav-item href="https://www.fabeook.com"  target="_blank"><font-awesome-icon :icon="`fa-brands fa-facebook`"/></b-nav-item>
                <b-nav-item href="https://www.twitter.com"  target="_blank"><font-awesome-icon :icon="`fa-brands fa-twitter`"/></b-nav-item>
                <b-nav-item href="https://www.tiktok.com"  target="_blank"><font-awesome-icon :icon="`fa-brands fa-tiktok`"/></b-nav-item>
              </div>
          </b-navbar-nav>
        </b-collapse>

      </b-navbar>
    </div>
    {{ /*END HEADER */ }}

    <div id="page"></div>
    <FirstPage v-if="this.target_page==='Home' && Object.keys(this.firebase_data).length"/>
    <SecondPage v-if="this.target_page==='Servizi'"/>
    <ThirdPage v-if="this.target_page==='Team'"/>
    <FourthPage v-if="this.target_page==='Eventi'"/>
    <FifthPage v-if="this.target_page==='Contatti'"/>
    <SixthPage v-if="this.target_page==='Prodotti'"/>
    <SeventhPage v-if="this.target_page==='Preferiti'"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import FirstPage from './components/FirstPage.vue';
import SecondPage from './components/SecondPage.vue';
import ThirdPage from './components/ThirdPage.vue';
import FourthPage from './components/FourthPage.vue';
import FifthPage from './components/FifthPage.vue';
import SixthPage from './components/SixthPage.vue'
import SeventhPage from './components/SeventhPage.vue';
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs, getDoc, doc} from 'firebase/firestore/lite';
import $ from "jquery";

// Follow this pattern to import other Firebase services
// import { } from 'firebase/<service>';

// TODO: Replace the following with your app's Firebase project configuration
const firebaseConfig = {
  apiKey: "AIzaSyCcxuN_ToTYSmdAK57gGQxgzXt8o-sAtjs",
  authDomain: "hulahoop-58ede.firebaseapp.com",
  projectId: "hulahoop-58ede",
  storageBucket: "hulahoop-58ede.appspot.com",
  messagingSenderId: "1036895608174",
  appId: "1:1036895608174:web:8ebf4e39942d01ba10f57f",
  measurementId: "G-6F6N0QWH4E"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Get a list of cities from your database
async function getData(key) {
  const data_ref = doc(db, 'data', 'data');
  const data_snap = await getDoc(data_ref);
  const data = data_snap.data()
  return data;
}

//DO NOT READ IF ALREADY IN LOCAL DATA
let data = getData('slides').then((result)=>{return JSON.parse(JSON.stringify(result))})
console.log(data)
  //load firebase data
  


export default {
  name: 'App',
  components: {
    FirstPage,
    SecondPage,
    ThirdPage,
    FourthPage,
    FifthPage,
    SixthPage,
    SeventhPage
  },
  data(){
    return{
      target_page:String,
      firebase_data:Object,
      start:true,
      isMobile:Boolean
    }
  },
  beforeMount(){

  },
  mounted(){
    this.isMobile = navigator.userAgent.toLowerCase().match(/mobile/i);
    console.log("MOBILE",this.isMobile)


    console.log(this.$el.querySelector(".navbar > .navbar-toggler.collapsed"), this.$el.querySelector(".navbar > .navbar-toggler.not-collapsed"))
    this.$el.querySelector("#coin").addEventListener("transitionstart", ()=>{
       this.$el.querySelector("#coin").style.animation="none"

      })
    this.$el.querySelector("#coin").addEventListener("transitionend", ()=>{
      this.$el.querySelector("#coin").style.animation="rotate3d 8s linear infinite"
      this.$el.querySelector("#coin").style.animationPlayState="initial"
    })

    data.then((result)=>{
    this.firebase_data=JSON.parse(JSON.stringify(result))
    this.target_page='Home' //first page
    console.log("MOUNTED", this.isMobile, this.firebase_data)

        this.$el.querySelector(".navbar > .navbar-toggler").addEventListener('click', ()=>{
        //move coin to left when toggler is not-collapsed
          if (window.innerWidth<990){
        console.log(this.$el.querySelector(".navbar > .navbar-toggler.collapsed"), this.$el.querySelector(".navbar > .navbar-toggler.not-collapsed"))
        //move left



        if (this.$el.querySelector(".navbar > .navbar-toggler.not-collapsed")===null){
                  if(window.innerWidth<500){
                    this.$el.querySelector("#coin").style.marginLeft="-25vw"

                  }else{
                    this.$el.querySelector("#coin").style.marginLeft="-25vw"

                  }
                  this.$el.querySelector("#coin").style.rotate="-360deg"
                  
                  this.$el.querySelector("#coin").style.transition="all 1s "




                }
        if (this.$el.querySelector(".navbar > .navbar-toggler.collapsed")===null){
                  if(window.innerWidth<500){
                    this.$el.querySelector("#coin").style.marginLeft="0vw"

                  }else{
                    this.$el.querySelector("#coin").style.marginLeft="10vw"

                  }
                  this.$el.querySelector("#coin").style.rotate="360deg"

                  this.$el.querySelector("#coin").style.transition="all 1s"

                    }

          }
          
      })
          //click twice to adjust bootstrap classes
      this.$el.querySelector(".navbar > .navbar-toggler").click()
      setTimeout( ()=> this.$el.querySelector(".navbar > .navbar-toggler").click(),100 )
    

      //new event listner: clickling on image === clicking on .navbar-toggler
      this.$el.querySelector("#coin").addEventListener("click", ()=>{
        this.$el.querySelector(".navbar > .navbar-toggler").click()
      })
    })
  
    
  },
  methods: {
    hide_dropdown(el){
      el.style.display="none"
    }

  
  },
  watch:{
    target_page: function(){
      console.log(document.querySelectorAll('.header_btn'))
      let header_btns=document.querySelectorAll('.header_btn_active')
      header_btns.forEach((el,i)=>{
        header_btns.item(i).className = header_btns.item(i).className.replace("_active","")
      })

      let active_btn= document.querySelector(`#${this.target_page.toLowerCase()}_btn`)
      active_btn.className= active_btn.className+"_active"

      if(this.start===false && window.innerWidth<=990){      
        this.$el.querySelector('.navbar-toggler').click()
        let toggleable_div= this.$el.querySelector('.container.navbar-collapse.collapse')
        toggleable_div.style.display="none"

      }else{
        this.start=false
      }


    },
    firebase_data: function(){
      console.log("FIREBASE DATA LOADED: ",this.firebase_data,  JSON.parse(JSON.stringify(this.firebase_data)))

      //hide empty social card
      let social_els=this.$el.querySelectorAll(".for_social")
      console.log("SOCIAL ELS", social_els)

      social_els.forEach((d,i)=>{
        if (social_els.item(i).src=""){
          social_els.style.backgroundColor="trapnsarent"
        }
      })
    }
  }
}
</script>


<style>
:root{
  --body_bg:rgba(255, 105, 105,0.6);
  --body_bg_dark:rgba(253, 221, 221, 0.507)

}

body{
  background-color: var(--body_bg) !important;
}


.carousel-item{
  width:100%;
  max-height: 600px;
  overflow: hidden;
}







.carousel-item > img{
  width: 50%;
  max-height: 100%
  
}
.header_btn{
  background-color: transparent;
  border-color: transparent ;
  font-family: Ink Free;
  font-size: 25px;
  transition: 0.5s;
  color:var(--body_bg_dark)

}

#coin_cont{
  margin-left: 3%;
  max-height: 132px;
  margin-right: -25%!important;
  margin-top:0%;
  margin-bottom: 1%!important;
  
}

.header_btn:hover{
  color: white;
  font-size: 28px;

  transition: 0.5s;
}



.carousel-control-next, .carousel-control-prev{
  background-color: rgba(255,255,255,0);
  text-align: left;
  transition: 1s;

}

.carousel-control-next:hover, .carousel-control-prev:hover{
  background-color: rgba(255,255,255,0.5);
  text-align: left;
  height: 100%;
  transition: 0.3s;

}

.header_btn_active{
  background-color: transparent;
  border-color: transparent ;
  font-family: Ink Free;
  font-size: 30px;
  color:white;
  border-bottom-color: rgb(254, 226, 226);
  border-bottom-style:double;
  border-bottom-width:100%;
  
  transition:0.5s;
  
  

}


h1,h3,h4{
  font-family: Ink Free;
  font-weight: bolder;
  text-shadow: black 1px 1px 1px;
}

.nav-link{
  font-size: 25px!important;
}

.carousel-caption{
  background-color: rgba(0, 0, 0, 0.268);
  border-radius: 3em;
  max-height: 650px;
}



.for_social_sub{
  background-color: var(--bs-danger);
  border-radius: 50%;
  width: 35px;
  text-align: center;
  border: rgb(248, 188, 188) 3px solid;

}

.for_social_sub_empty{
  display: none;
}

.for_social_sub > *> svg > path{
  fill: rgb(248, 188, 188);
}

.card_social_cont{
  display: flex;
    flex-direction: row;;
    width: 50%;
    text-align:justify;
    justify-content: space-evenly;
    position: absolute;
    top:-15px;
    left:25%!important;
    margin-top:-0%;
    font-size:20px;
    z-index: 99999!important;


}

.navbar-toggler.collapsed, .navbar-toggler{
  position:absolute;
  top:0;
  width: 25%;
  right: 0;
  height: 100%;
 
}

.navbar-toggler.not-collapsed{
  height: 95%;
}

#team_btn::before, #prodotti_btn::before, #servizi_btn::before{
  content:"";
  border:1px solid var(--body_bg);
  height: 25%;
  width:  0%;
  margin-right: 15%;
}

#eventi_btn,#preferiti_btn,#contatti_btn{
  margin-left: 2%;
}
@keyframes rotate3d {
            0% {
                transform: perspective(1000px) rotateY(360deg);
            }

            100% {
                transform: perspective(1000px) rotateY(0deg);
            }
        }

#coin{
  animation: rotate3d 8s linear infinite;
  margin-bottom: -5%!important;
  margin-left: -40%;
  background: rgba(255,255,255,0.7);
  border-radius: 50%;
  border: var(--body_bg) 25px solid;
  width: 550px;
  position: relative;
  z-index:1

}

#home_btn{
  margin-left: 0%;
}



@media only screen and (min-width: 990px) {

  #header_pages_cont{
  display: flex;
  flex-direction: row;
  
}

  #header_social_cont{
  display: flex;
  flex-direction: row;
  position: absolute;
  right:25px;
}



.header_title{
  display: none;
 }

 .arrow{
  display: block;
  background-color: rgba(255,255,255,0.5);
 }



 #coin{
  animation: rotate3d 8s linear infinite;
  margin-top: -38%!important;
  margin-left: -40%!important;
  background: rgba(255,255,255,0.7);
  border-radius: 50%;
  border: var(--body_bg) 25px solid;
  scale: 0.2 !important;
  object-fit: contain;
  object-position: center;
  box-sizing:content-box; 
}

}

@media only screen and (max-width: 990px) {
  #header_pages_cont{
  display: flex;
  flex-direction: column;
}
#header_social_cont{
  width: 50%;
  position: absolute;
  display: flex;
  flex-direction: row;
  text-align: justify;
  justify-content: space-evenly;
  left: 30%;
  bottom:0

}
.header_title{
  display: none;
  font-family: Ink Free;
  font-size: 35px;
  font-weight: bolder;
  text-align: center;
 }
 .arrow{
  display: none;
 }

 #nav-collapse{
  margin-left: 43%;
  margin-bottom:50px;
  margin-top:-15%;
 }

 #coin{
  margin-left: 20%;
  transform:scale(1);
}

#header_social_cont{
  background-color: var(--body_bg);
  width: 100%;

}

* > #header_social_cont{
  width: 100%!important;
  left:0px !important
}


}




@media only screen and (max-width: 990px) {
  #nav-collapse{
  margin-left: 35%;
  margin-bottom:50px;
  margin-top:-15%;

 }
 .card_social_cont{
  margin-top: 3%!important;
 }
 .for_social_sub{
  transform:scale(0.8);
 }

 p{
  margin-top: 0px!important;
 }



 #coin{
  scale: 0.8;
  border-width: 7px;
  animation: rotate3d 8s linear infinite;
  width: 150px;
}


@media(orientation:portrait){
  #coin_cont{
  margin-left: 32%!important;
  width: 50%!important;
 }
 .navbar-toggler{
  display: none!important;
 }
 .navbar-collapse{
  margin-left: 35%!important;
 }
 h3{
  margin-top: 5%!important;
}
.card_social_cont{
  top:-10%;
}

.carousel-item{
  width:100%;
  max-height: 200px !important;
  overflow: hidden;
}


.carousel-item > img{
  width: 50%;
  max-height: 10%!important
  
}
#team_btn::before, #prodotti_btn::before, #servizi_btn::before{
  position:absolute;
  content:"";
  border:1px solid var(--body_bg);
  height: 0%;
  width: 50%;
  left:25vw
}


}
@media(orientation:landscape){
  #coin_cont{
  margin-left: 32%!important;


 }
 .navbar-toggler{
  display: none!important;
 }
 .navbar-collapse{
  margin-left: 42%!important;
 }

 h3{
  margin-top: 2%!important;
}
.card_social_cont{
  top:-10%;
}

.carousel-item{
  width:100%;
  max-height: 350px !important;
  overflow: hidden;
}


.carousel-item > img{
  width: 50%;
  max-height: 100%
  
}
}
#team_btn::before, #prodotti_btn::before, #servizi_btn::before{
  position:absolute;
  content:"";
  border:1px solid var(--body_bg);
  height: 0%;
  width: 50%;
  left:25vw
}

}
.navbar{
  display: flex;
  flex-direction: row;
  width: 100%!important;
}



</style>

