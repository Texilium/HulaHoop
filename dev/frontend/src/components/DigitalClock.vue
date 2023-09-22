
<template>
    <span>
        <h4>{{ this.title }}</h4>
        <p>{{ this.hour +":"+ this.minute }}</p>
    </span>
</template>


<script>
//      ADD: CLOCK OPEN, CURRENT HOUR, CLOCK CLOSE
//      AN HORIZONTAL LIST WITH SQARES FOR EACH DAY OF THE WEEK: RED CLOSED, GREEN OPEN
export default{
    name:"DigitalClock",
    props:{
        title:String,
        hour:String,
        minute:String
    },
    data(){
        return{

        }
    },
    mounted(){      


    },
    methods:{

    },
    watch:{

    }
}
</script>

<style scoped>

    *{
        font-family: Orbitron
    }
</style>
