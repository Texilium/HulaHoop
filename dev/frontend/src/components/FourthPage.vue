<template>
    <section id="fourth_page_cont" class="page_cont">
        <div id="events_metacont">

                <span id="calendar_cont">
                    <b-dropdown id="event_type_dropdown" :text=" 'Filtra eventi per tipo: '+this.type_selected" ref="type_dropdown" class="m-md-2" >
                                <button :class="type_selected===type_ ?'type_opt_active' :'type_opt'" v-for="(type_,i) in this.types" :key="i.toString()+type_" @click="update_type(type_)">{{type_}}</button><br>

                            </b-dropdown>
                    <b-calendar id="calendar" v-model="date" :date-disabled-fn="dateClass" locale="it" block>
                        <div class="d-flex calendar_btns_cont" dir="ltr">
                        <b-button
                            size="sm"
                            variant="primary"
                            class="ml-auto"
                            @click="setToday"
                        >
                            Imposta oggi
                        </b-button>
                        <b-button
                            size="sm"
                            variant="danger"
                            class="ml-auto"
                            v-if="date"
                            @click="clearDate"
                        >
                            Deseleziona
                        </b-button>
                        </div>
                    </b-calendar>
                </span>

                <span id="events_cont">
                    <h2><span id="event_number">{{this.n_events}}</span> eventi trovati</h2>
                    <div>
                        <b-card-group deck>
                            <div v-for="(event,i) in this.displayable_events" :key="i+event" style="margin-bottom:3%;">

                   
                            <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top style="height: 250px" :class="'event_type_'+types.indexOf(event['type'])"
                            >
                         
                                
                                <b-card-text>
                                This is a wider card with supporting text below as a natural lead-in to additional content.
                                This card has even longer content than the first to show that equal height action.
                                </b-card-text>
                                
                                <div class="card_social_cont_event">
                                    <div class="for_social" v-for="(social_key,j) in Object.keys(event).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                                        <span  :class="social_key!=='' ?'for_social_sub_5' :'for_social_pub_empty_5'" v-if="event[social_key]!==''"> <a :href="event[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </span> 
                                    </div>
                                </div>

                             
            

                            <div class="card-footer">
                                    <small class="text-muted">{{event.date}}</small>
                                </div>
                            </b-card>
                            
                                     </div>
                        </b-card-group>
                        </div>
                </span>

        </div>
    </section>
</template>

<script>
export default{
    name:"FourthPage",
    props:{},
    data(){
        return{
            date:'',
            events:[],
            displayable_events:[],
            type_selected:"",
            types:[],
            type_colors:{},
            colors:[],
            start:true,
            n_events:0
            
        }
    },
    mounted(){
        this.colors=["rgba(220, 53, 70, 1)","rgba(13, 202, 240, 1)", "rgba(255, 81, 7, 1)","rgba(40, 167, 70, 1)","rgba(130, 23, 184, 1)"]


        this.events= this.$parent.firebase_data["slides"]["events"]
        this.displayable_events=this.events
        this.types=["Tutti",... this.events.map(d=>d['type']).sort().filter(this.onlyUnique)]
        for (let i=0;i<this.types.length;i++){
            this.type_colors[this.types[i]]=this.colors[i]
        }
        console.log("DICT", this.types_colors)
        this.type_selected=this.types[0]
        this.n_events=this.displayable_events.length
        


    },
    methods:{
        onlyUnique(value, index, array) {
        return array.indexOf(value) === index;
        },
        update_type(type){
            this.type_selected=type
            this.$nextTick(()=>this.$el.querySelectorAll(".type_opt").forEach((d,i)=> this.$el.querySelectorAll(".type_opt").item(i).style.backgroundColor="transparent"))
            this.$nextTick(()=>this.$el.querySelector(".type_opt_active").style.backgroundColor=this.type_colors[type])
        }
        ,
        setToday() {
        const now = new Date()
        this.date = new Date(now.getFullYear(), now.getMonth(), now.getDate())
      },
      clearDate() {
        this.date = ''
        let calendar_cells = this.$el.querySelectorAll(".b-calendar-grid-body span")
        console.log("CALENDAR CELLS",calendar_cells)
        calendar_cells.forEach((d,i)=>{
                calendar_cells.item(i).classList.remove("btn-light")            
        })
      },
        dateClass(ymd, date) {
        //date-info-fn works in bootstrapvue 4.0.0 and not in 4.4.0. Chaging it resolves this but makes other things worst.
        //so disable all dates that are not in data
        //selecting them by year, month and date!
        //pass this function to :date-disabled-fn
        console.log(date.getDate().toString())

            let day = date.getDate().toString().length>1 ?date.getDate().toString() :"0"+date.getDate().toString()
            let yr=date.getFullYear()
            let month=(date.getMonth()+1).toString().length>1 ?(date.getMonth()+1).toString() :"0"+(date.getMonth()+1).toString()

            

            const event_dates= this.events.map(d=>d["date"])
            const event_types= this.events.map(d=>d["type"])
            console.log(event_dates, `${yr}-${month}-${day}`)


            if (event_dates.includes(`${yr}-${month}-${day}`)){
                if (this.type_selected!=="Tutti"){
                    if(this.events.filter(f=>f["type"]===this.type_selected && f["date"]===`${yr}-${month}-${day}`).length>0){  //if 0 then equals to false I guess
                        return false
                    }else{
                        return true
                    }
                }
                return false //false is do not disable
            }else{
                return true
            }

      }
    },
    watch:{
        date: function (){
            console.log("DATE", this.date)
            if (this.date!==""){
                this.displayable_events = this.events.filter(f=>f["date"]==this.date)
            }else{
                 this.displayable_events = this.events
            }

            if (this.type_selected!=="Tutti"){
                this.displayable_events=this.displayable_events.filter(d=>d["type"]===this.type_selected)

            }
            this.n_events=this.displayable_events.length

        },

        type_selected: function(){
            this.displayable_events= this.date==="" ?this.events :this.events.filter(f=>f["date"]===this.date)
            let calendar_cells = this.$el.querySelectorAll(".b-calendar-grid-body")
            console.log("CALENDAR",calendar_cells, this.colors, this.type_colors, this.type_selected)
            if (this.type_selected==="Tutti"){
                this.displayable_events=  this.date==="" ?this.displayable_events :this.displayable_events.filter(f=>f["date"]===this.date)
                //calendar_cells.forEach((d,i)=>calendar_cells.item(i).style.backgroundColor="blue")
            }else{
                this.displayable_events= this.displayable_events.filter(f=>f["type"]===this.type_selected)
            }
            calendar_cells.forEach((d,i)=>calendar_cells.item(i).style.backgroundColor=this.type_colors[this.type_selected])

            if(this.start===false){
                this.$el.querySelector("#event_type_dropdown__BV_toggle_").click()
                
            }else{
                this.start=false
            }
            this.$el.querySelector("#event_type_dropdown__BV_toggle_").style.backgroundColor=this.type_colors[this.type_selected]
            this.$el.querySelector(".b-calendar-grid-caption").style.backgroundColor=this.type_colors[this.type_selected]
            this.$el.querySelector(".b-calendar-grid-weekdays").style.backgroundColor=this.type_colors[this.type_selected]
            

            

            this.$el.querySelector(".b-calendar-grid-caption").style.color="white"
            this.$el.querySelector(".b-calendar-grid-weekdays").style.color="white"

            this.n_events=this.displayable_events.length

        }
    }
}
</script>

<style>
    :root{
        --color_5:rgba(220, 53, 70, 0.5);
        --color_1:rgba(13, 202, 240, 0.5);
        --color_2:rgba(255, 81, 7, 0.5);
        --color_3:rgba(40, 167, 70, 0.5);
        --color_4:rgba(130, 23, 184, 0.501);
        --orange: "#F68657";
        --green: #70bd63;
        --bg: #f8c985;


    }
    h2{
        font-family: INK FREE;
        font-size: 30px!important;
        font-weight: bolder!important;
    }

    .btn-light{
        background: transparent!important;
    }
    .b-calendar-grid-body{
        background-color: rgba(13, 202, 240, 0.4);
    }

    .b-calendar .b-calendar-nav .btn{
    background-color: white!important;
}

    .b-calendar-footer{
        width: 75%;
        margin-left: 12%;
    }

    #events_cont{
        width: 80%;
        text-align: center;
        padding: 3%;

    }

    #event_cont > .card{
        text-align: center;
        height: 100%;
        font-size: 80%;
    }

    .card-img-top{
        max-width: 10em;
        margin-top:12px;
        margin-left:3%;
        position: relative;
        border-radius: 100% !important;
        z-index: 9999;
        border:1px solid rgba(0, 0, 0, 0.504)
    }

    .card-body{
        position: absolute;
        text-align: center;
        margin-left: 25%;
        height: 100%;
        background-color: rgba(255,255,255,0.5);
    }

    .event_url_cont{
        position: absolute;
        bottom: 30px;
        text-align: center;
        width: 100%;
    }
    .card-footer{
        position: absolute;
        bottom: 0;
        width: 100%;
        left:0;

    }

    .card-text{
        width: 70%;
        height: 140px;
    margin-left: 15%;
    background-color: rgba(255, 255, 255, 0.344);
    padding:1%;
    border: 1px black solid;
    border-radius: 0.3rem
    }

    .card_social_cont_event{
        position: absolute;
        right:20px;
        top:15px;
        text-align: justify;
        justify-content: space-evenly;

        
    }
    .calendar_btns_cont{
        display: flex;
        flex-direction: row;
        width:100%;
    }

    .calendar_btns_cont >button{
        width: 100%!important;
        flex:1
    }
    
    #event_type_dropdown> .dropdown-menu.show{
        position: absolute;
        display: flex!important;;
        flex-direction: column;
        width: 300px;
    }
    .b-calendar-grid.form-control.h-auto.text-center{
        background-color: var(--color_5)!important;
    }

    .col.p-0:not([aria-disabled]) > span{
        color: white !important;
    }

    #calendar_cont{
        position: absolute;
    }

    #event_type_dropdown__BV_toggle_{
        min-width:200px;
        margin-left:-3px
        
    }





    .type_opt, .event_opt_active{
        width: 100%;
        background-color: transparent;
        border: transparent;
    }

    .type_opt_active{
        background-color: #0d6efd;
        color: white;
    }
    #type_dropdown{
        display: flex;
        flex-direction: column;
        width: 110%!important;
        background-color: white
        ;
    }
    .b-calendar{
        margin-top: 35px;
        margin-left:5px;
        
    }

    .event_type_1{
        background-color: var(--color_1)!important

    }
    .event_type_2{
        background-color: var(--color_2)!important

    }
    .event_type_3{
        background-color: var(--color_3)!important

    }
    .event_type_4{
        background-color: var(--color_4)!important

    }.event_type_5{
        background-color: var(--color_5)!important

    }

    
    @media only screen and (min-width: 990px) {     
    #events_metacont{
            display: flex;
            flex-direction: row;
            width: 100%;
        }
    
    .b-calendar,#event_type_dropdown__BV_toggle_{
        position: fixed;
        width: 300px;

    }

    
    #events_cont{
        margin-left: 280px;
    }


}

@media only screen and (max-width: 990px) {
     #events_metacont{
            display: flex;
            flex-direction: column;
            width: 100%;
        }


    #events_cont > .card{
        height: 250px ;
    }

    #events_cont{
        width: 100%;
        padding: 3%;
    }


    .card-body{
        padding: 3%;
    }

    

    .card-text{
        width: 80%;
        height: 150px;
        margin-top:10px;
        margin-left: 0%;
        max-height: 150px;
        overflow: scroll;
        
    }

    .card-img-top{
        max-width: 80px;
        margin-left: 7%;
        margin-top:12px;
        position: absolute;
        border-radius: 100% !important;
        
    }

    .card-title{
        margin-left: -20%;
    }

    .event_url_cont{
        margin-left: -20%
    }

    .card-footer{
    }
    
    #calendar_cont{
        position:relative;
    }
    #event_type_dropdown__BV_toggle_{
        width: 100%;
    }
    .b-calendar{
        margin-top: 0px;
    }

    .dropdown-menu.show{
        width: 100% !important;
    }
    #calendar_cont{
        width: 85%!important;
        margin-left: 7%;
    }

    #event_type_dropdown{
        width: 75%;
        margin-left: 12%!important;
    }
}


@media only screen and (max-width:550px){
    .card-img-top{
        max-width: 60px;
        min-width: 40px;
        margin-left: 3%;
        margin-top:12px;
        position: absolute;
        border-radius: 100% !important;
        
    }

    #calendar_cont{
        width: 85%!important;
        margin-left: 7%;
        margin-top:3%
    }

    #event_type_dropdown{
        width: 75%;
        margin-left: 15%;
    }
}

    
.for_social_sub_5{
  background-color: transparent;
  border-radius: 50%;
  width: 40px!important;
  text-align: center;
  border: rgb(248, 188, 188) 0px solid;

}

.for_social_sub_empty_5{
  display: none;
}

.for_social_sub_5 > *> svg > path{
  fill: var(--bs-danger);
}

@media(orientation:landscape){
    h2{
        margin-top: 3%!important;
        margin-bottom:3%!important
    }
}

@media(orientation:portrait){
    h2{
        margin-top: 4%!important;
        margin-bottom:4%!important
    }
}
</style>
