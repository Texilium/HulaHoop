<template>
    <section id="second_page_cont" class="page_cont">
        <div id="second_page_text">
            <div id="text_service1_cont" class="text_el">
                <h1 id="service1_title" class="title_">Ma cosa facciamo di preciso?</h1>
                <div id="service1" class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
            </div>

            <div id="text_gonfiabili_cont" class="text_el">
                <h1 id="gonfiabili_title" class="title_">I gonfiabili</h1>
                {{/*START CAROUSEL */ }}
                <div id="carousel_cont2.1">
                    <b-carousel
                    id="carousel-2.1"
                    v-model="slide_gonfiabili"
                    :interval=this.interval_gonfiabili
                    controls
                    indicators
                    fade
                    background="transparent"
                    img-width="1024"
                    img-height="480"
                    style="text-shadow: 1px 1px 2px #333;"
                    @sliding-start="onSlideStart(sliding_gonfiabili)"
                    @sliding-end="onSlideEnd(sliding_gonfiabili)"
                    >
                    <!-- Text slides with image -->
                    <span  v-for="(gonfiabile,i) in this.gonfiabili" :key="i.toString()+gonfiabile.caption">
                        <b-carousel-slide
                        :caption="gonfiabile.caption"
                        :text="gonfiabile.text"
                        :img-src="gonfiabile.image"
                        >
                        
                        <div class="card_social_cont">
                            <div class="for_social" v-for="(social_key,j) in Object.keys(gonfiabile).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                                <div :class="social_key!=='' ?'for_social_sub' :'for_social_pub_empty'" v-if="gonfiabile[social_key]!==''"> <a :href="gonfiabile[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </div> 
                            </div>
                        </div>

                        </b-carousel-slide>
                    </span>
                    
                
                </b-carousel>

                </div>
                {{/*END CAROUSEL */ }}
                <div id="gonfiabili" class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
            </div>

            <div id="text_mascotte_cont" class="text_el">
                <h1 id="mascotte_title" class="title_">Le mascotte</h1>
                {{/*START CAROUSEL */ }}
                <div id="carousel_cont2.2">
                    <b-carousel
                    id="carousel-2.2"
                    v-model="slide_mascotte"
                    :interval=this.interval_mascotte
                    controls
                    indicators
                    fade
                    background="transparent"
                    img-width="1024"
                    img-height="480"
                    style="text-shadow: 1px 1px 2px #333;"
                    @sliding-start="onSlideStart(sliding_mascotte)"
                    @sliding-end="onSlideEnd(sliding_mascotte)"
                    >
                    <!-- Text slides with image -->
                    <span  v-for="(mascotte,i) in this.mascotte" :key="i.toString()+mascotte.caption">
                        <b-carousel-slide
                        :caption="mascotte.caption"
                        :text="mascotte.text"
                        :img-src="mascotte.image"
                        >
                        
                        <div class="card_social_cont">
                            <div class="for_social" v-for="(social_key,j) in Object.keys(mascotte).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                                <div :class="social_key!=='' ?'for_social_sub' :'for_social_pub_empty'" v-if="mascotte[social_key]!==''"> <a :href="mascotte[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </div> 
                            </div>
                        </div>

                        </b-carousel-slide>
                    </span>
                    
                
                </b-carousel>

                </div>
                {{/*END CAROUSEL */ }}
                <div id="mascotte" class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
            </div>

            <div id="text_foto_cont" class="text_el">
                <h1 id="foto_title" class="title_">Il servizio fotografico</h1>
                {{/*START CAROUSEL */ }}
                <div id="carousel_cont2.3">
                    <b-carousel
                    id="carousel-2.3"
                    v-model="slide_fotografia"
                    :interval=this.interval_fotografia
                    controls
                    indicators
                    fade
                    background="transparent"
                    img-width="1024"
                    img-height="480"
                    style="text-shadow: 1px 1px 2px #333;"
                    @sliding-start="onSlideStart(sliding_fotografia)"
                    @sliding-end="onSlideEnd(sliding_fotografia)"
                    >
                    <!-- Text slides with image -->
                    <span  v-for="(foto,i) in this.foto" :key="i.toString()+foto.caption">
                        <b-carousel-slide
                        :caption="foto.caption"
                        :text="foto.text"
                        :img-src="foto.image"
                        >
                        <div class="card_social_cont">
                            <div class="for_social" v-for="(social_key,j) in Object.keys(foto).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                                <div :class="social_key!=='' ?'for_social_sub' :'for_social_pub_empty'" v-if="foto[social_key]!==''"> <a :href="foto[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </div> 
                            </div>
                        </div>
                        </b-carousel-slide>
                    </span>
                    
                
                </b-carousel>

                </div>
                {{/*END CAROUSEL */ }}
                <div id="foto" class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
            </div>

            <div id="text_gadgets_cont" class="text_el">
                <h1 id="gadgets_title" class="title_">I nostri gadgets!</h1>
                <div id="gadgets" class="body_">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
                    cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
                     Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
                      Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.
                    Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
                </div>
                {{/*START CAROUSEL */ }}
                <div id="carousel_cont2.4">
                    <b-carousel
                    id="carousel-2.4"
                    v-model="slide_gadgets"
                    :interval=this.interval_gadegts
                    controls
                    indicators
                    fade
                    background="transparent"
                    img-width="1024"
                    img-height="480"
                    style="text-shadow: 1px 1px 2px #333;"
                    @sliding-start="onSlideStart(sliding_gadgets)"
                    @sliding-end="onSlideEnd(sliding_gadgets)"
                    >
                    <!-- Text slides with image -->
                    <span  v-for="(gadget,i) in this.gadgets" :key="i.toString()+gadget.caption">
                        <b-carousel-slide
                        :caption="gadget.caption"
                        :text="gadget.text"
                        :img-src="gadget.image"
                        >
                        
                        <div class="card_social_cont">
                            <div class="for_social" v-for="(social_key,j) in Object.keys(gadget).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                                <div :class="social_key!=='' ?'for_social_sub' :'for_social_pub_empty'" v-if="gadget[social_key]!==''"> <a :href="gadget[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </div> 
                            </div>
                        </div>

                        </b-carousel-slide>
                    </span>
                    
                
                </b-carousel>

                </div>
                {{/*END CAROUSEL */ }}
            </div>

            
        </div>
    </section>
</template>

<script>
export default{
    name:"SecondPage",
    props:{},
    data(){
        return{
            interval_gonfiabili:4000,
            slide_gonfiabili:0,
            sliding_gonfiabili:null,

            interval_mascotte:4000,
            slide_mascotte:0,
            sliding_mascotte:null,

            interval_fotografia:4000,
            slide_fotografia:0,
            sliding_fotografia:null,

            interval_gadegts:4000,
            slide_gadgets:0,
            sliding_gadgets:null,
            
            gonfiabili:Array,
            mascotte:Array,
            foto:Array,
            gadgets:Array
        }
    },
    mounted(){
    this.gonfiabili= this.$parent.firebase_data["slides"]["gonfiabili"]
    this.mascotte= this.$parent.firebase_data["slides"]["mascotte"]
    this.foto= this.$parent.firebase_data["slides"]["foto"]
    this.gadgets= this.$parent.firebase_data["slides"]["gadgets"]



    },
    methods:{
        onSlideStart(sliding) {
        sliding = true

      },
      onSlideEnd(sliding) {
        sliding = false
      },
    },
    watch:{

    }
}
</script>

<style>
@media only screen and (max-width:500px){
    .card_social_cont{
    margin-top:3%!important
}
}


</style>
