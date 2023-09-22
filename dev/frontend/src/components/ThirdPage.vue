<template>
    <section id="third_page_cont" class="page_cont">
        <div id="team_container">
            
            {{ /*IF i is even img to right, else image to left*/ }}
            {{/*START CARD*/ }}

           <div class="container flex flex-col items-center justify-center p-4 mx-auto space-y-8 sm:p-10">
			<h1 class="text-4xl font-bold leadi text-center sm:text-5xl">Il nostro team</h1>
			<p class="max-w-2xl text-center dark:text-gray-400">At a assumenda quas cum earum ut itaque commodi saepe rem aspernatur quam natus quis nihil quod, hic explicabo doloribus magnam neque, exercitationem eius sunt!</p>
			<div class="card_metacont">
                <div v-for="(team_el,i) in this.team_els" :key="i.toString()+team_el.real_name" style="margin-left: 15%;" class="card_cont">
				<div class="team_card">
					<img alt="" class="team_img" :src="team_el.image">
					<p class="team_name">{{team_el.real_name}}</p>
					<p class="team_role">{{team_el.role}}</p>
                    <div class="card_social_cont">
                        <div class="for_social" v-for="(social_key,j) in Object.keys(team_el).filter(f=>f.includes('social_'))" :key="i.toString()+social_key+j.toString()">
                        <span  :class="social_key!=='' ?'for_social_sub' :'for_social_pub_empty'" v-if="team_el[social_key]!==''"> <a :href="team_el[social_key]" target="_blank"><font-awesome-icon :icon="`fa-brands fa-${social_key.replace('social_','')}`"/> </a> </span> 
                        </div>
                    </div>
				</div>
				
			</div>
            </div>
            
		</div>
           
            {{/*END CARD*/ }}
        </div>
        
    </section>
</template>

<script>
export default{
    name:"ThirdPage",
    props:{},
    data(){
        return{
            team_els:[],
            social_icons:{
                "facebook":"fa fa-facebook",
                "tiktok":"fa-brands fa-tiktok",
                "instagram":"fa fa-instagram",
                "twitter":"twitter"
            }
        }
    },
    mounted(){
        this.team_els= this.$parent.firebase_data["slides"]["team_els"]

    },
    methods:{

    },
    watch:{

    }
}
</script>

<style scoped>
#third_page_cont{
    text-align: center;
}

.team_img{
    width: 6rem;
    height: 6rem;
    border-radius: 50%;
    background-position:center;
    align-self: center;
    vertical-align: middle;
    object-fit: cover;
    margin-top: -15%;
}

.card_metacont{
    display:flex;
    flex-direction: row;
    width: 90%;
    flex-wrap: wrap;
    position: absolute;
    margin-left: 1vw;
}
.team_card{
    display:flex;
    flex-direction: column;
    width: 20em;
    height: 11em;
    min-width: 10em ;
    background-color: white;
    border: 1px solid black;
    min-width: 100%;
    margin-top:25%;
    border-radius: 0.375rem;
   
}

.card_social_cont{
    display: flex;
    flex-direction: column;
    position: inherit;
    width: 1em;
    text-align:justify;
    justify-content: space-evenly;
    margin-left:290px;
    margin-top:-125px

}

.team_name{

    font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: bolder;
    font-size: 1.3rem;
}

.team_role{
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;

}



@media only screen and (max-width:1000px){
    .card_metacont{
       width:50%;
       margin-left: 15%;
    }
}

@media only screen and (max-width:700px){
    .card_metacont{
       width:50%;
       margin-left: 5%;
    }
}

@media only screen and (max-width:500px){
    .card_metacont{
       width:50%;
       margin-left: 0%;
       
    }

    .card_social_cont{
        margin-top:-40%!important
    }
}

@media (orientation:landscape){
    .card_social_cont{
        margin-top: -40%!important;
    }
    
}
@media (orientation:portrait){
    .card_social_cont{
        margin-top: -40%!important;

    }
}


.for_social_sub{
  background-color: transparent;
  border-radius: 50%;
  width: 40px!important;
  text-align: center;
  border: rgb(248, 188, 188) 0px solid;

}

.for_social_sub_empty{
  display: none;
}

.for_social_sub > *> svg > path{
  fill: var(--bs-danger);
}

</style>
