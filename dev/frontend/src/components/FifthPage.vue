

<template>
    <section id="fifth_page_cont" class="page_cont">
        <h1 class="first_title">Quando contattarci</h1>
    <div id="hours_metacont">
    <b-container id="hours_cont" fluid >
        <div id="hours_subcont">

            <b-row>
            <b-col cols="6">

            </b-col>
            <b-col cols="4">
              Apre
            </b-col>
            <b-col cols="1">
              Chiude
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="6">Mattina</b-col>
            <b-col cols="4" class="digital_number open">
              8:00
            </b-col>
            <b-col cols="1" class="digital_number close">
                13:00
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="6">Pomeriggio</b-col>
            <b-col cols="4" class="digital_number open">
              17:00
            </b-col>
            <b-col cols="1" class="digital_number close">
                20:00
            </b-col>
        </b-row>

        </div>
      
        
    <div id="days_cont" class="hour_subcont" >
            <div v-for="day in this.days" :key="day" :class="work_days.includes(day) ?'open_day' :'close_day'">{{day}}</div>
    </div>
    </b-container>

</div>
<div id="sign_cont">
        <img id="open_sign" :src="this.current_sign_url" class="sign"/>
    </div>




    <b-container id="info_cont" fluid>
        <h1>Come contattarci</h1>
        <div class="info_subcont">
           <p><i class="fa fa-envelope" aria-hidden="true"> test@test.com</i></p>
            <p><i class="fa fa-phone" aria-hidden="true"> 345 3322111</i></p>
        </div>
    </b-container>


    <b-container id="line_cont" fluid>
        <h1>I nostri impegni</h1>

        <b-row>
            <b-col cols="12"  id="plot_div">
                
            </b-col>
        </b-row>
    </b-container>
    </section>
</template>

<script>
import DigitalClock from './DigitalClock.vue'
//      ADD: CLOCK OPEN, CURRENT HOUR, CLOCK CLOSE
//      AN HORIZONTAL LIST WITH SQARES FOR EACH DAY OF THE WEEK: RED CLOSED, GREEN OPEN
export default{
    name:"FifthPage",
    components:{
    },
    props:{},
    data(){
        return{
            events:[],
            types:[],
            type_colors:{},
            colors:[],
            days:["Lun","Mar","Mer","Gio","Ven","Sab","Dom"],
            work_days:["Lun","Mar","Mer","Gio","Ven"],
            open_hours:["8:00","17:00"],
            close_hours:["13:00","20:00"],
            current_sign_url:""
        }
    },
    mounted(){
        //check sign
        this.activity_is_open()

        this.colors=["rgba(220, 53, 70, 0.5)","rgba(13, 202, 240, 0.5)", "rgba(255, 81, 7, 0.5)","rgba(40, 167, 70, 0.5)","rgba(130, 23, 184, 0.5)"].reverse()
        this.events= this.$parent.firebase_data["slides"]["events"]
        this.types=[... this.events.map(d=>d['type']).sort().reverse().filter(this.onlyUnique)]
        for (let i=0;i<this.types.length;i++){
            if(this.types[i]!=="Tutti"){
                this.type_colors[this.types[i]]=this.colors[i]
            }else{
                this.type_colors["Tutti"]=this.colors[-1]
            }
        }
        console.log("DICT", this.types_colors)
        this.create_stacked_area()

    },
    methods:{
        activity_is_open(){
 
            var options = {'weekday': 'short', 'month': '2-digit', 'day': '2-digit'};
            let curr_date= new Date()
            let hour= curr_date.getHours()
            let weekday= curr_date.toLocaleString("it-IT",options).slice(0,1).toUpperCase() + curr_date.toLocaleString("it-IT",options).slice(1,).split(" ")[0]
            let open_url="open.jpg"
            let close_url="close.jpg"

            console.log()
            if (!this.work_days.includes(weekday)){ //if not work day
                this.current_sign_url=close_url
            }else{
                console.log("TESTT", (+this.open_hours[0].split(":")[0]>=hour && hour <+this.close_hours[0].split(":")[0]),  (+this.open_hours[1].split(":")[0]>=hour && hour <+this.close_hours[1].split(":")[0]))
                if( (hour>=+this.open_hours[0].split(":")[0] && hour <+this.close_hours[0].split(":")[0]) || //if hour is comprised between morning hours or afternoon hours
                    (hour>=+this.open_hours[1].split(":")[0] && hour <+this.close_hours[1].split(":")[0])
                ){
                    this.current_sign_url=open_url
                }else{
                    this.current_sign_url=close_url
                }
            }

            console.log("ACTIVITY", weekday, hour, weekday)

        },
        onlyUnique(value, index, array) {
        return array.indexOf(value) === index;
        },
       create_stacked_area(){
        var plotDiv = document.getElementById('plot_div');
        let traces=[]
        
        //group data by type
        //LINE
        let line_trace={
            "x":[],
            "y":[],
            "name":"test",
            "type":"scatter",
            "showlegend":false,
            "marker":{"color":"rgba(13, 202, 240, 0.4)"}
            

            
        }
        let unique_dates=this.events.map(d=>d["date"]).filter(this.onlyUnique)

        unique_dates.forEach((d,i)=>{
            console.log("D", d)
            let temp_filt= this.events.filter(f=>f["date"]==d)
            let temp_y= temp_filt.length
            console.log("TEMP", temp_y)
            line_trace["x"].push(d)
            line_trace["y"].push(temp_y)

           
        })

        console.log("unique_dates", unique_dates)
        traces.push(line_trace)

        //BAR
        this.types.forEach(type_=>{
            let filt_events=this.events.filter(f=>f["type"]==type_).sort()
            let filt_dates
            if (window.innerWidth>990){
                filt_dates= filt_events.map(d=>d["date"]).sort().filter(this.onlyUnique)
            }else{
                filt_dates= filt_events.map(d=>d["date"]).sort().filter(this.onlyUnique).reverse()

            }
            console.log("FILT", filt_events, filt_dates)
            //create a trace as {x:dates, y:counts, stackgroup: type}
            let temp_trace={"x":[],"y":[], "name":type_, type:'bar', marker:{color:this.type_colors[type_]}}
            filt_dates.forEach((date_,j)=>{
                let final_events= filt_events.filter(z=>z["date"]===date_)
                temp_trace["x"].push(date_)
                temp_trace["y"].push(final_events.length)
            })
            temp_trace["text"]=temp_trace["y"]
            traces.push(temp_trace)

        })

        console.log("traces", traces)
        var day= new Date().getDate()
            var month= new Date().getMonth()+1
            var year= new Date().getFullYear()
            var today= `${year}-${month}-${day}`

            var shapes= [{
            type: 'line',
            x0: today,
            y0: 0,
            x1: today,
            yref: 'paper',
            y1: 1,
            line: {
            color: 'grey',
            width: 1.5,
            dash: 'dot'
            }
        }]

        let screen_width=window.innerWidth
        var annots
        if(screen_width>=990){
             annots=[ {
                x: today,
                y: 0,
                xref: 'x',
                yref: 'y',
                text: 'Oggi<br>'+today,
                showarrow: true,
                arrowhead: 7,
                ax: 0,
                ay: -40
                }]
            }else{
                annots=[ {
                x: 0,
                y: today,
                xref: 'x',
                yref: 'y',
                text: 'Oggi: '+today,
                showarrow: true,
                arrowhead: 7,
                ax: 70,
                ay: 0
                }]
            }

        //invert x and y in case of small scree
        //invert x and y in case of small scree

            console.log("traces", traces)

            traces.forEach((trace,i)=>{
                let temp_trace= {...trace}
                if (screen_width<=990){
                    temp_trace["x"]=trace["y"]
                    temp_trace["y"]=trace["x"]

                    temp_trace["orientation"]="h"
                }else{
                    temp_trace["orientation"]="v"
                }
                traces[i]=temp_trace
            })

            if(screen_width<=990){
                annots["y"]=2
                annots["x"]=today
                annots["ax"]=50
                annots["ay"]=1000
            }



            var layout = {barmode: 'stack', showlegend:"true", legend: {"orientation":"v", "xanchor":"center"}, margin: {l: 50,r: 50, b: 50, t: 0, pad: 5}, annotations:annots}
            if (true){ 
                layout["legend"]["orientation"]="h"
                layout["legend"]["y"]="1.1"
                layout["legend"]["x"]="0.5"


            }

            if (screen_width<=700){
                layout["legend"]["y"]="1.3"
                layout["legend"]["x"]="0.2"

            }

        
            console.log("traces", traces)

        try{
        Plotly.newPlot('plot_div', traces, layout=layout, {"displayModeBar":false});
        }catch{
            
        }
            },
    onResize(){
        try{
            window.addEventListener("resize", this.create_stacked_area)

        }catch{

        }
    }
    },
    watch:{
        types:function(){
            this.onResize()
            //this.create_stacked_area()
        }
    }
}
</script>

<style scoped>
h1{
    background: var(--bs-danger);
    margin-bottom: 1px;
    width: 65%;
    margin-left: 20%;
    border-radius: 0.5em 0.5em 0em 0em;
    color:white
}



p{
    font-size: 20px;
}

i{
    text-decoration: underline ;
    text-underline-offset: 5px;
}

#fifth_page_cont{
    text-align: center;
    width: 100%;
}

#line_cont .row{
    width: 100%;
       
}
#plot_div{
    width: 65%;
    margin-left: 20%;
    
}



#info_cont{
    margin-top:50px!important;
    margin-bottom:25px;
    padding: 2%;
}

.info_subcont{
    background-color: white!important;
    width: 65%;
    margin-left: 20%;
    height: 150px;
    padding: 2%!important;
    
}

.info_subcont:first-child{
    margin-top: -5%;
}

#hours_cont{
    width: 40%!important;
    margin-left:22.5%!important;
}

#hours_metacont{
    background-color: white;
    width: 65%;
    margin-left: 20%;
}

.digital_number{
    font-family: Orbitron;
}

.close{
    color: rgb(228, 37, 37);
    text-shadow: rgb(228, 37, 37) 3px 2px 3px ;
}
.open{
    color: rgb(37, 228, 43);
    text-shadow: rgb(37, 228, 43) 3px 2px 3px  ;
}

.close_day{
    background-color: rgb(228, 37, 37)!important;
    box-shadow: rgb(228, 37, 37) 3px 2px 3px ;
}
.open_day{
    background-color: rgb(37, 228, 43);
    box-shadow: rgb(37, 228, 43) 3px 2px 3px  ;
}
#days_cont{
    width:100%;
    display:flex;
    flex-direction: row;
    text-align: justify;
    justify-content: space-evenly;
    margin-left: 25%;
}

#days_cont > *{
    margin-right: 5%;
    padding:3%;
    color: white;
    width: 50px;

}

.first_title{
    margin-top:2%
}

@keyframes swing {

    10% {
        transform: translateX(-25px);
        transform: rotate(25deg)
    }
    20% {
        transform: translateX(25px);
        transform: rotate(-25deg)

    }
    30% {
        transform: translateX(-15px);
        transform: rotate(25deg)
    }
    40% {
        transform: translateX(15px);
        transform: rotate(-25deg)

    }
    50% {
        transform: translateX(-15px);
        transform: rotate(15deg)
    }
    60% {
        transform: translateX(15px);
        transform: rotate(-15deg)

    }
    70%{
        transform: translateX(-5px);
        transform: rotate(5deg)
    }
    80%{
        transform: translateX(5px);
        transform: rotate(-5deg)
    }
    90%{
        transform: translateX(0px);
        transform: rotate(2deg)
    }
    100%{
        transform: translateX(0px);
        transform: rotate(0deg)
    }
    }
#days_cont{
    background-color: white;
}
.sign{
    width:100px;
    transform: rotate(15deg);
    -moz-animation: swing 2s infinite;
    -webkit-animation: swing 2s infinite;
    animation: swing 4s ease;
    margin-top:-20px;
    position: absolute;
    z-index:-9999;
    transform:rotate(0deg);
    align-content: center;
    margin-left: -2.5rem;
    width:7rem;

}
#sign_cont{
    height: 100px!important;
    width: 65%;
    margin-left:20%;
    background-color: white;
    position:relative;
    z-index: -99999;


}





@media only screen and (max-width: 990px) {


    
    #hours_cont{
    width: 60%!important;
    margin-left:-17%!important;
    
}

#hours_subcont{
    width: 100%!important;
    margin-left: 70%!important;
}
#sign_cont{
    height: 150px;
    width: 65%;
 

}

#days_cont{
    width:100%;
    display:flex;
    flex-direction: row;
    text-align: justify;
    justify-content: space-evenly;
    margin-left: 70%;
}
}


@media only screen and (max-width: 500px) {

    #hours_cont{
    transform: scale(0.7);
    width: 70%!important;
    margin-left:-13%!important;
}

#hours_subcont{
    margin-left: 5em!important;
}
#days_cont{
    width:100%;
    display:flex;
    flex-direction: row;
    text-align: justify;
    justify-content: space-evenly;
    margin-left: 70%;
}

#sign_cont{
    height: 150px;
    width: 65%;
    margin-left:20%;
    margin-top:-2%;
}

.sign{
    margin-left: -27%;
}

#info_cont{
    margin-top: 30%;
}

}

@media(orientation:portrait){
    .info_subcont{
    background-color: white!important;
    width: 65%;
    margin-left: 20%;
    height: 150px;
    padding: 8%!important;
    
}

}

@media(orientation:landscape){
    .info_subcont{
    background-color: white!important;
    width: 65%;
    margin-left: 20%;
    height: 120px;
    
}

.info_subcont{
    padding: 2%!important
}

}
</style>
