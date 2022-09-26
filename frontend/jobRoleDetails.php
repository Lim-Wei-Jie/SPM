<?
?>

<!DOCTYPE html>
<html lang="en" data-theme="pastel">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/happy.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>LJPS</title>
    <script src="https://unpkg.com/vue@next"></script>
    <script type="module" src="../src/main.js"></script>
  </head>
  <body>
    <!--start of vue instance-->
    <div id="app1">
        <!-- Navigation Bar -->
        <div class="navbar bg-base-100">
            <div class="navbar-start">
                <div class="dropdown">
                <label tabindex="0" class="btn btn-ghost btn-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
                </label>
                <ul tabindex="0" class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
                    <li><a>Job Roles</a></li>
                    <li><a>My Learning Journey</a></li>
                    <li><a>Team Completion Status</a></li>
                </ul>
                </div>
            </div>
            <div class="navbar-center">
                <a class="btn btn-ghost normal-case text-xl">LJPS</a>
            </div>
            <div class="navbar-end">
                <!-- v-if to check if the user is logged in and what type of user-->
                <label for="my-modal-4" class="btn modal-button">LOG IN</label>
                <!-- <h5>Hello! Bobby Lim</h5>
                <label for="my-modal-4" class="btn modal-button">LOG OUT</label> -->
            </div>
        </div>
        <!-- end of navigation Bar -->
        <h3 class="mx-6 my-2 font-bold text-xl">Current Job Roles ({{numOfJobRoles()}})</h3>
        <div class="form-control">
            <div class="grid grid-cols-2">
                <div class="input-group mx-5 mb-3">
                <!--Search bar-->
                <input type="text" style="width: 300px;" placeholder="Search Job Role…" class="input input-bordered" v-model='queryName'/>
                <button class="btn btn-square" v-on:click="searchJob()">
                    <!-- v-on:change.prevent="searchJob()" v-on:click.prevent="searchJob()"-->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                </button>
                </div>
                <div class='place-self-end mr-1'>
                    <button class="btn">Add new</button>
                </div>
            </div>
        
        
            <!-- display available job roles need to use v-for-->
            <div class="bg-base-200 mx-4 my-6 p-4" v-if='hasJob'>
                <div class="grid grid-cols-3 gap-6 ">
                    <div class="bg-gray-200 hover:bg-red-400 hover:text-white p-3 rounded-md font-bold" v-for="jobRole in jobRoles">
                        <!--need to go to the specific job role page-->
                        <!-- <a :href=' "resturant_details.php#" + restaurant.name'> -->
                            {{jobRole}}
                        <!-- </a> -->
                    </div>
                    <!-- <div class="bg-gray-200 hover:bg-red-400 hover:text-white p-3 rounded-md font-bold">Software Engineer</div>
                    <div class="bg-gray-200 hover:bg-red-400 hover:text-white p-3 rounded-md font-bold">Software Engineer</div>
                    <div class="bg-gray-200 hover:bg-red-400 hover:text-white p-3 rounded-md font-bold">Software Engineer</div> -->
                </div>    
            </div>
            <div class="bg-base-200 mx-4 my-6 p-4" v-else>
                <h2 class="font-bold text-l ">There is no job role of {{queryName}}</h2>
    
            </div>
        </div>
    </div>
    </body>

    <!--start of vue-->
    <script>
        const app= Vue.createApp({
            data(){
                return{
                    num: 0,
                    jobRoles:['Software Engineer', 'Senior Software Engineer', 'Technical Manager', 'Web Developer'],
                    jobRole: '',
                    queryName: '',
                    hasJob: true,

                }
            },
            methods:{
                numOfJobRoles(){
                    for (let i=0; i < this.jobRoles.length; i++){
                       this.num ++;
                    }
                    return this.num;
                },
                searchJob(){
                    if(!this.jobRoles.includes(this.queryName)){
                        hasJob = false;
                    }
                }
            }
        })
    //  created(){
    // var arr = window.location.href.split('#');} 
        const vm =app.mount('#app1');
    </script>

</html>
