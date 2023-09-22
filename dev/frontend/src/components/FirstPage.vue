<template>
    <section id="first_page_cont" class="page_cont">
        {{/*START CAROUSEL */ }}
        <div id="carousel_cont" ref="carousel_first_page" v-if="this.slides.length">
            <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval=this.interval
            controls
            indicators
            fade
            background="transparent"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
            >
            <!-- Text slides with image -->
            <span  v-for="(slide_,i) in this.slides" :key="i.toString()+slide.caption">
                <b-carousel-slide
                :caption="slide_.caption"
                :text="slide_.text"
                :img-src="slide_.image"
                >
                <div class="card_social_cont">
                        <div class="for_social" v-for="(social_key,j) in Object.keys(slide_).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                        <div :class="social_key!=='' ?'for_social_sub' :'for_social_pub_empty'" v-if="slide_[social_key]!==''"> <a :href="slide_[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </div> 
                        </div>
                    </div>
                </b-carousel-slide>
            </span>
            <div id="down_arrow_cont">
            <div class="arrow bounce" id="arrow1">
            <a class="fa fa-arrow-down fa-2x" href="#first_page_text"></a>
        </div>
        <div class="arrow bounce" id="arrow2">
            <a class="fa fa-arrow-down fa-2x" id="arrow2" href="#first_page_text"></a>
        </div>
        </div>
           
            </b-carousel>

        </div>
        {{/*END CAROUSEL */ }}

        <div id="first_page_text">
            <div id="text_hulahoop_cont" class="text_el">
                <h1 id="hulahoop_title" class="title_">Che cos'è Hula Hoop?</h1>
                <div id="hulahoop_text" class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
            </div>

            <div id="text_animationgroup_cont" class="text_el">
                <h1 id="groupanimation_title"  class="title_">Di cosa si occupa?</h1>
                <div id="groupanimation_text"  class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
            </div>

            <div id="text_animationgroup_cont" class="text_el">
                <h1 id="groupanimation_title"  class="title_">Con chi collabora?</h1>
                <div id="groupanimation_text"  class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                    <br>
                    Vai alla sezione <button class="link_btn" v-on:click="go_to_page('Team')">Team</button> per saperne di più!
                    
                </div>
            </div>

            <div id="text_servizi_cont" class="text_el">
                <h1 id="servizi_title"  class="title_">Che servizi offriamo?</h1>
                <div id="servizi_text"  class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                    <br>
                    Vai alla sezione <button class="link_btn" v-on:click="go_to_page('Servizi')">Servizi</button> o alla sezione <button class="link_btn" v-on:click="go_to_page('Eventi')">Eventi</button> per saperne di più!
                    
                </div>
            </div>

            <div id="text_servizi_cont" class="text_el">
                <h1 id="servizi_title"  class="title_">Dove trovarci</h1>
                <div id="servizi_text"  class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                    <br>
                    Vai alla sezione <button class="link_btn" v-on:click="go_to_page('Contatti')">Contatti</button> per saperne di più!
                    
                </div>
                    <div id="map_cont">
                        <div id="tile_handler_cont">
                            <b-dropdown id="tile_dropdown" :text=" 'Stile: '+this.tile_selected" ref="tile_dropdown" class="m-md-2" variant="outline-primary">
                                <button :class="tile_selected===key ?'tile_opt_active' :'tile_opt'" v-for="(key,i) in Object.keys(this.map_tiles)" :key="i.toString()+key" @click="update_selected_tile(key)">{{key}}</button><br>

                            </b-dropdown>
                        </div>
                        <div id="map"></div>
                    </div>
                    

            </div>
        </div>
        

        
    </section>
</template>

<script>  
export default{
    
    name:"FirstPage",
    props:{},
    data(){
        return{
            interval:4000,
            slide:0,
            sliding:null,
            slides:[],
            map:[],
            map_tiles:{
                "Satellite":"http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                "Standard":'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
                
            },
            tile_selected:"Satellite",
            data_loaded:false
        }
    },
    mounted(){
         /*
        setTimeout(() => {
                this.scrollTo();
                }, "100");
       
       //read home slides (cannot be done in a generalized function, as e.g. "this.slide" is not modified)
       fetch("home_slides.json")
        .then((res)=>res.json())
        .then((json)=>{
            this.slides=json["slides"]
        }).catch((e)=>console.log("ERR", e))
        */
       this.slides= this.$parent.firebase_data["slides"]["slides"]
        console.log(this.slides)

       //init map
        this.initMap()




        
    },
    methods:{
        scrollTo() {
      this.$refs.carousel_first_page.scrollIntoView();
    },
        onSlideStart(slide) {
        this.sliding = true

      },
      onSlideEnd(slide) {
        this.sliding = false
      },

      go_to_page(page){
        //alert("a")
        //this doesn't work because the listener must be set as a prop of a component, not in the component itself (i.e., App.vue)
        //opt for scroll approach instead
        //this.$emit('change-page-from-child',page_n)
        this.$parent.target_page = page
        window.scrollTo({top:0, left:0, behavior:"smooth"})
      },
      initMap() {
        var map = L.map('map').setView([41.14952,16.40628], 18);
       L.tileLayer(this.map_tiles[this.tile_selected], {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
        }).addTo(map);

        var marker = L.marker([41.14952,16.40628]).addTo(map).bindPopup("Siamo qui!<br>Via Alemanni, 68, Corato").openPopup();
        //preserve map for destroying it after
        marker
        this.map= map
      },

      update_selected_tile(key){
        this.tile_selected=key
      }
            
      
    },
    watch:{
        tile_selected: function(){
            this.map.off();
            this.map.remove();
            this.initMap()
            this.$el.querySelector("#tile_dropdown__BV_toggle_").click()

        },

    }
}
</script>

<style>
    #carousel_cont{
        width: 100%;
        position: relative;
    }

    #first_page_text, #second_page_text{
        width: 100%;
        position: absolute;
        margin-top: 1%;
        text-align: justify;
        width: 75%;
        margin-left: 15%;
        text-justify: inter-word;
    }

    ol > li{
        width: 20px;
        height: 20px;
        margin-left: 1vw;
        margin-right: 1vw;
        margin-bottom:5vh;
        background-color: grey;
        border: 1px black solid;
        color: transparent;
        font-size: 0px;
        border-radius: 50%;
        border:transparent;
        box-shadow: rgba(0, 0, 0, 0.56) 0px 12px 7px 2px;

        transition: 500ms ease-in; /*see this.interval */



    }

    
    ol > li.active{
        width: 25px;
        height: 25px;
        margin-left: 2vw;
        margin-right: 2vw;
        background-color:rgba(231, 16, 16, 0.615);
        border: transparent;
        color: black;
        font-size: 0px;
        text-align: center;
        border-radius: 50%;
        box-shadow: rgba(125, 60, 60, 0.615) 0px 12px 7px 2px;;
        animation: glow 1s ease-in-out infinite alternate;

        


        transition: 700ms;
        border: transparent;

    }

    ol > li:hover{
        color:black;
        font-size:10px; 
    }

    ol > li.active:hover{
        color:black;
        font-size:16px; 
        margin-left: 3vw;
    }

    ol{
        margin-bottom: 70px;
    }


    

  
   

    .arrow {
    text-align: center;
    position: absolute;
    color: black;
    background-color: white;
    border-radius: 50%;
    padding: 1%;
    z-index: 999;
    border: var(--body_bg) 7px solid;
    

    }
    #arrow1{
        left:150px;
        bottom:50px;
    }

    #arrow2{
        bottom:50px;
        right:150px;
    }

    .fa-arrow-down{
        color:var(--bs-danger) ;
    } 

    .bounce {
    -moz-animation: bounce 2s infinite;
    -webkit-animation: bounce 2s infinite;
    animation: bounce 2s infinite;
    }


    #down_arrow_cont{
        width: 100%;
    }



    
    @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-30px);
    }
    60% {
        transform: translateY(-15px);
    }
    }


    .carousel-caption{
        position: absolute;
        top:5%;
    }

    .carousel-caption>p{
        margin-top: 15%;
    }

    .slide_url_cont{
        position: absolute;
        text-align: center;

        bottom: 50px;
        left:40%;
    }


    .title_{
        text-align: center;
    }

    .link_btn{
        background-color: transparent;
        border: transparent;
        color: black;
        padding: 0;
        text-decoration: underline;
        cursor: pointer;
    }
    #map { height: 500px; }
    .tile_opt, .tile_opt_active{
        width: 100%;
        background-color: transparent;
        border: transparent;
    }

    .tile_opt_active{
        background-color: #0d6efd;
        color: white;
    }

    #tile_handler_cont{
        position: absolute;
        z-index: 999;
        left:50px
    }
    #tile_dropdown{
        display: flex;
        flex-direction: column;
        width: 110%!important;
        background-color: white
        ;
    }




    @media only screen and (max-width: 990px) {
        ol > li{
        margin-left: 1vw;
        margin-right: 1vw;
        margin-bottom:0vh;
     }

     .slide_url_cont{
        bottom:0px
     }
    }

 


    


</style>
