<template>
    <!-- eslint-disable -->
    <NavBar/>
    <div class="container mx-auto my-8 flex flex-col">
        <!-- Breadcrumbs -->
        <div class="text-sm breadcrumbs">
            <ul>
                <li @click="HomePage"><a>Home</a></li> 
                <li @click="JobRolePage"><a>Job Role</a></li> 
                <li> {{roleDetailsName}} </li>
            </ul>
        </div>
        <!-- Role Name -->
        <div class="grid grid-cols-2 my-4">
            <p class="text-3xl font-bold underline underline-offset-8">
                {{roleDetailsName}}
            </p>
        </div>
        <!-- Role Desc -->
        <div class="space-y-2 my-4 w-4/6">
            <p class="font-medium text-lg">
                Job Role Description
            </p>
            <p>
                {{roleDetailsDesc}}
            </p>
        </div>
        <!-- Skills -->
        <div class="space-y-3 my-4">
            <p class="text-2xl font-medium">
                Skills
            </p>
            
            <div v-for="skill in skillsList" class="bg-gray-300 rounded-lg my-6 p-8 space-y-4">
                <p class="text-lg font-normal">
                    {{ skill.skill_name }}
                </p>
                <div class="grid grid-cols-3 gap-6">
                    <div v-if="skill.courses_selected != []" class="flex " v-for="course in skill.courses_selected">
                        <label class="btn btn-lg w-11/12 modal-btn" for="my-modal">
                            {{ course }}
                        </label>

                    
                    </div>
                    <li v-for="course in skill.courses_available" class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3">
                        <div class="flex justify-between">
                            <div>
                                <p class="font-medium">{{ course.course_id}} - {{ course.course_name }}</p>
                                <p class="font-light">{{ course.course_desc }}</p>
                            </div>
                            <input type="checkbox" v-model="selectedCourses" :id="course.course_id" :value="course.course_id" class="checkbox" />
                        </div>
                        
                    </li>
                </div>
            </div>
        </div>
        <!-- send edited data back-->
        <button class="btn btn-outline btn-success" @click="createRegis(skillsList, selectedCourses, staffID, roleDetailsID, ljpsID)">Create Learning Journey</button>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { onBeforeMount, ref, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails, getCoursesBySkill, getSkillsByRole, createLJ2, getAllRegistrationNo, getLJs, getAllLJPSNo } from "@/endpoint/endpoint.js";

//route back for breadcrumb
const router = useRouter()
function HomePage() {
    router.push('/staff')
}
function JobRolePage() {
    router.push('/staff/searchRole')
}


const props = defineProps({
    jobRoleName: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleName } = toRefs(props)
const roleName = JSON.parse(JSON.stringify(jobRoleName))._object.jobRoleName

//JOB ROLE
const roleDetailsName = ref()
const roleDetailsID = ref()
const roleDetailsDesc = ref()
const staffID = ref('130003')
const skillsList = ref([])
const selectedCourses = ref([])
const ljpsID = ref()

;(async() => {
try {
    var res1 = await getAllLJPSNo()
    ljpsID.value = res1

    //ROLE DETAILS
    const role = await getRoleDetails(roleName)
    roleDetailsName.value = role.Role_Name
    roleDetailsID.value = role.Role_ID
    roleDetailsDesc.value = role.Role_Desc

    const LJ = await getLJs(staffID.value)
    var x = LJ[roleDetailsID.value]
    
    if ( x.length != 0 ){
        alert('A learning journey was set for this job role. You cannot set more than 1 learning journey for each job role.')
        router.push('/staff/searchRole') 
    }
    

    //SKILLS DETAILS
    const skills = await getSkillsByRole(roleDetailsID.value)
    for(var skill of skills){
        var courses = await getCoursesBySkill(skill.Skill_ID)
        var courseList = []
            for (var course of courses) {
                if (course.Course_Status == "Active") {
                    var courseDetails = {
                        course_name: course.Course_Name,
                        course_id: course.Course_ID,
                        course_desc: course.Course_Desc
                    }
                    courseList.push(courseDetails)
                }
            }

        var skillDetails = {
            skill_id: skill.Skill_ID,
            skill_name: skill.Skill_Name,
            skill_desc: skill.Skill_Desc,
            courses_available: courseList,
            courses_selected: []
        }
        skillsList.value.push(skillDetails) 
    }
}
catch(err) {
    console.log(err);
}
})();

var regID = 0
onBeforeMount(
    async() => {
    await getAllRegistrationNo()
    .then((res) => {
        if (regID == 0) {
            regID += res
        }
    }).catch((err) => {
        console.log(err);
    });
})();

function createRegis(skillsList, selectedCourses, staffID, roleID, ljpsID) {
    if (selectedCourses.length == 0) {
        alert('Please select at least one course for each skill.')
    } else {
        var temp = 0
        for (var skill of skillsList) {
            var temp1 = 0
            for (var avail_course of skill.courses_available) {
                var avail_course_ID = avail_course.course_id
                for (var sel_course of selectedCourses) {
                    if (sel_course == avail_course_ID) {
                        temp1 +=1
                    }
                }
            }
            if (temp1 >= 1) {
                temp += 1
            } 
        }

        if( skillsList.length != temp) {
            alert('Please select at least one course for each skill.')
        } else {
            //add registration
            ;(async() => {
            try {
                //get LJPS_ID
                var res = await createLJ2(staffID, roleID, ljpsID)
                var newLjpsID = res.data.LJPS_ID
                

                for (var courseID of selectedCourses) {
                    addReg(regID, courseID, staffID)
                    regID+=1
                }

                for (var courseID of selectedCourses) {
                    addToLJ(courseID, ljpsID)
                }
                
                //route to staff page
                router.push('/staff') 
            }
            catch(err) {
                console.log(err);
            }
            })();
        }
    }
}

//add to registration
function addReg(regID, courseID, staffID) {
    var regStatus = 'Registered'
    var completionStatus = 'Ongoing'
    ;(async() => {
        await fetch(`${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/Registration/addRegis/${regID}/${courseID}/${staffID}/${regStatus}/${completionStatus}`)
        .then((res) => {
            console.log(res)

        }).catch((err) => {
            console.log(err);
        });
    })();
}

function addToLJ(courseID, ljpsID) {
    ;(async() => {
        await fetch(`${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/AddLJAssignCourse/${courseID}/${ljpsID}`)
        .then((res) => {
            
        }).catch((err) => {
            console.log(err);
        });
    })();
}
</script>

<style scoped>
</style>