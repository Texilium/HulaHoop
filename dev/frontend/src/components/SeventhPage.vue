<template>
    <section id="seventh_page_cont" class="page_cont">
        <div id="product_state_handler_cont" fluid>
          

            <font-awesome-icon :class="this.state_selected==='Cart' ?'state_icon_active' :'state_icon'" icon="fa-solid fa-heart"  @click="()=>this.state_selected='Cart'"/>
          
        </div>

        <div id="type_selector_cont">
            <b-dropdown id="type_dropdown" :text="this.type_selected" ref="type_dropdown" class="m-md-2" variant="danger">
                <button :class="type_selected===key ?'type_opt_active' :'type_opt'" v-for="(key,i) in this.type_opts" :key="i.toString()+key" @click="update_selected_type(key)">{{key}}</button><br>

            </b-dropdown>
        </div>
        <h3 class="el_counter"><span id="cart_number">{{this.displayable_shop_els.filter(d=>this.onlySaved(d)).length}}</span> prodotti salvati</h3>

       

        <div id="cart_cont">
            <div class="for_shop" v-for="(el, i) in this.displayable_shop_els.filter(d=>this.onlySaved(d))" :key="'cart_'+i.toString()">
            <img class="for_shop_img" :src="el['image']"/>
            <h3>{{el["caption"] }}</h3>
            <p class="for_shop_type">{{el['type']}}</p>
            <div class="for_shop_footer">
                <div class="heart_icon_active">
                    <font-awesome-icon icon="fa-solid fa-heart" @click="(e)=>{
                        handle_heart_and_eye(e);
                        //ADD LOCALSTORAGE LOGIC TO ADD AND REMOVE THE EL
                        if(check_heart_state(el)){
                            save_el(el)
                        }else{
                                                //also remove the html el
                                remove_html_el(e)
                                remove_el(el)

   
                        }

                        }" ></font-awesome-icon>
                </div>
                <div class="cart_icon">
                    <font-awesome-icon  icon="fa-solid fa-shopping-cart"></font-awesome-icon>
                </div>
            </div>
            <div class="for_shop_descr">{{ el['text'] }}</div>
            

            </div>
        </div>
    </section>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {isEqual} from 'lodash'

  
export default{
    name: "SeventhPage",
    props: {},
    data() {
        return {
            slides: [],
            type_selected: "",
            data_loaded: false,
            state_selected: "Shop",
            type_opts:[],
            displayable_shop_els:[],
            saved_items:[],
            n_clicks:0

        };
    },
    mounted() {
        this.slides = this.$parent.firebase_data["slides"];
        this.type_opts= ["tutti",... Object.keys(this.slides).filter(f=>["gonfiabili","mascotte", "gadgets"].includes(f))]
        console.log(this.slides);
        if (window.localStorage.getItem("loved_els")===null){
            console.log("NO LOCAL STORAGE",)
            window.localStorage.setItem("loved_els",JSON.stringify([]))
        }else{
            this.saved_items= JSON.parse(window.localStorage.getItem("loved_els"))
        }
        console.log("LOCAL STORAGE", JSON.parse(window.localStorage.getItem("loved_els")))
        this.n_saved=this.displayable_shop_els.filter(d=>this.onlySaved(d)).length


        this.type_selected="tutti"
    },
    methods: {
        remove_html_el(e){
         e.target.parentElement.parentElement.parentElement.parentElement.remove()
          },
        onlySaved(el){
            return JSON.parse(window.localStorage.getItem('loved_els')).some(d=>isEqual(d,el))
        },
        onlyUnique(value, index, array) {
            return array.indexOf(value) === index;
        },
        isEqual_(d,el){
            return isEqual(d,el)
        },
        check_heart_state(el){
            return ! JSON.parse(window.localStorage.getItem('loved_els')).some(d=>isEqual(d,el))
        },
        save_el(data){
            window.localStorage.setItem('loved_els', JSON.stringify([...JSON.parse(window.localStorage.getItem('loved_els')), data]))
        },
        remove_el(data){
            window.localStorage.setItem('loved_els',JSON.stringify(JSON.parse(window.localStorage.getItem('loved_els')).filter(f=>!isEqual(f,data))))
            let counter= this.$el.querySelector("#cart_number")
            this.$nextTick(()=>{
                counter.innerHTML= (+counter.innerHTML - 1).toString()

            })
        },
        scrollTo() {
            this.$refs.carousel_first_page.scrollIntoView();
        },
        go_to_page(page) {
            //alert("a")
            //this doesn't work because the listener must be set as a prop of a component, not in the component itself (i.e., App.vue)
            //opt for scroll approach instead
            //this.$emit('change-page-from-child',page_n)
            this.$parent.target_page = page;
            window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
        },
        update_selected_type(key) {
            this.type_selected = key;
        },

        handle_heart_and_eye(e){
            if(e.target.tagName==="path"){
                let target=e.target.parentElement.parentElement
                console.log(target, e.target, e.target.tagName)
                if (target.getAttribute("class").includes("_active")){
                    //ACTIVE
                    target.setAttribute("class", target.getAttribute("class").replace("_active",""))

                } else{
                    //NOT ACTIVE
                    target.setAttribute("class", target.getAttribute("class")+"_active")

                }

                

            }
          
        },

    },
    watch: {
        type_selected: function () {

            if(this.type_selected==="tutti"){
                //take only necessary slides
                let new_slides=[]
                Object.keys(this.slides).map(k=>{
                    if(this.type_opts.includes(k)){
                        let new_els= this.slides[k]
                        new_els.forEach((each,i)=>{
                            new_els[i]["type"]=k
                        })
                        this.displayable_shop_els= [...this.displayable_shop_els, ...new_els].filter(this.onlyUnique)
                    }
                })
            }else{
                let new_els=this.slides[this.type_selected]
                new_els.forEach((each,i)=>{ new_els[i]["type"]=this.type_selected })
                this.displayable_shop_els= new_els.filter(this.onlyUnique)
            }

            //UPDATE ELS AFTER TYPE FILTERING

            //close dropdown
            if(this.$el.querySelector(".dropdown-menu.show")){
                this.$el.querySelector(".btn.dropdown-toggle.btn-danger").click()

            }
            console.log("DISPLAYABLE SHOP,",this.displayable_shop_els)
        },

    
        
    },
    components: { FontAwesomeIcon }
}
</script>

<style scoped>
:root{
    --body_bg:rgba(255, 105, 105,0.6);
    --eye_off:rgba(220, 237, 255, 1);
    --eye_on:rgba(91, 124, 153, 1)

}


.page_cont{
    width: 75%;
    margin-left:40%;
}

#product_state_handler_cont{
    width:35%;
    text-align: center;
    margin-top: 3%;



}

#product_state_handler_cont>*{
    color:var(--bs-danger);
    width:30px;
}

#product_state_handler_cont > div{
    width: 30%;
}

.state_icon{
 font-size: 30px;
color: white;
}

 .state_icon_active{
    color:var(--bs-danger);
    font-size: 30px;
 }

 .state_active_cont{
    margin-left: -30%;
    width: 100%;
    text-align:  center;
    margin-top: 3%;
 }


#type_selector_cont{
    width: 50%;
    margin-left:-10%
}
#seventh_page_cont >>> .dropdown-menu.show{
    width: 100%!important;
}

.type_opt_active{
   background-color: var(--bs-danger)!important;
   width: 100%;
}

#shop_cont, #cart_cont{
    margin-bottom: 25%;
    width: 100%;
    height:100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    position: absolute;
    left:0;
}


.for_shop{
    background-color: white;
    width:25%;
    margin-left:5%;
    object-fit: contain;
    margin-top:3%;
    max-height: 500px;

}

.for_shop_img{
    top:0;
    left:0;
    width: 25vw;
    height: 25vh;
    scale: 0.8;

}

h3, .for_shop_type, .for_shop_descr{
    text-align: center;
}

.for_shop_type{
    font-family: italics;
    color: var(--bs-danger);
}

.for_shop_descr{
    display: none;
    height: 0%;


    
}


.for_shop:hover .for_shop_descr{
    display: block;
    height: 100%;
    max-height: 20%;
    max-width: 100%;
    overflow: scroll;
    background-color: white;
}


.for_shop_footer{
    width: 100%;
    display: flex;
    flex-direction: row;
    background: white;
}

.for_shop_footer div{
    width: 50%;
    margin-bottom: 5%;
    text-align: center;
}

.for_shop_footer div[class$='_active']{
    width: 50%;
    text-align: center;
}

.el_counter{
    text-align: center;
    width:35%;
    font-size:25px;
}

@keyframes rotate3d {
            0% {
                transform: perspective(1000px) rotateY(360deg);
            }

            100% {
                transform: perspective(1000px) rotateY(0deg);
            }
        }

@keyframes pulse {
            0% {
                transform: scale(1.3);
                
            }

            10% {
                transform: scale(1);

            }

            25%{
                transform: scale(1.27)
            }


            90%{
                transform: scale(1)
            }

            100% {
                transform: scale(1.3);
            }
        }

@keyframes tilt {
            0% {
                transform: rotate(-10deg);
                
            }

            50% {
                transform: rotate(10deg);

            }

            100% {
                transform: rotate(-10deg);
            }
        }

.heart_icon{
    width: 25%;
    flex:1;
    font-size: 30px;
    color:var(--body_bg)
}


.heart_icon_active{
    width: 25%;

    color:var(--bs-danger);
    font-size: 30px;
    animation: pulse 2s ease infinite 
}

.cart_icon{
    flex:1;
     width: 25%;

    font-size: 30px;
    color:rgb(89, 164, 244);

}


.cart_icon{
    width: 25%;

        font-size: 30px;

    color:var(--bs-info);

}
@media (orientation:portrait){
    .for_shop_img{
    top:0;
    width: 100vw;
    height: 25vh;
    scale: 0.8;

}
.for_shop{
    background-color: white;
    width:97%;
    margin-left:1.5vw;
    object-fit: contain;
    margin-top:3%;
    margin-right:1%;
    margin-bottom:20%

}
.btn.dropdown-toggle.btn-danger{
    width:110%!important;
    object-fit: contain!important;
}
}

@media (orientation:landscape){
    .for_shop_img{
    top:0;
    left:0;
    width: 25vw;
    height: 25vh;
    scale: 0.8;
    

}

.for_shop{

    margin-bottom:5%

}
}

</style>
