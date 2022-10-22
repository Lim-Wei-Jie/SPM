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
                    <div v-if="courses_selected != []" class="flex " v-for="course in skill.courses_selected">
                        <label class="btn btn-lg w-11/12 modal-btn" for="my-modal">
                            {{ course }}
                        </label>

                        <!-- modal pop up to delete course-->
                        <input type="checkbox" id="my-modal" class="modal-toggle" />
                        <div class="modal">
                            <div class="modal-box">
                                <h3 class="font-bold text-lg">{{ course }}</h3>
                                <div class="modal-action">
                                    <label for="my-modal" class="btn btn-outline btn-error" @click="deleteCourse(course, skill.skill_id, skillsList)">Remove Course</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <label for="addCourseModal" class="modal-btn btn btn-lg btn-outline w-11/12" @click="getAllCourses(skill.skill_id)">Add Course</label>
                    <!-- modal pop up to add course-->
                    <input type="checkbox" id="addCourseModal" class="modal-toggle" />
                    <div class="modal">
                        <div class="modal-box h-fit w-11/12">
                            <h3 class="font-bold text-lg">{{ skill.skill_name }}</h3>
                            <ul>
                                <li v-for="course in courseList" class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3">
                                    <div class="flex justify-between">
                                        <div>
                                            <p class="font-medium">{{ course.course_id}} - {{ course.course_name }}</p>
                                            <p class="font-light">{{ course.course_desc }}</p>
                                        </div>
                                        <input type="checkbox" v-model="selectedCourses" :id="course.course_id" :value="course.course_id" class="checkbox" />
                                    </div>
                                    
                                </li>
                            </ul>
                            <div class="modal-action">
                                <label for="addCourseModal" class="btn btn-outline btn-success" @click="addCourse(selectedCourses, skill.skill_id, skillsList)">Add Course</label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- send edited data back-->
        <label for="my-modal" class="btn btn-outline btn-success" @click="createLJ()">Create Learning Journey</label>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails, getCoursesBySkill, getSkillsByRole } from "@/endpoint/endpoint.js";

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

;(async() => {
    await getRoleDetails(roleName)
    .then((role) => {
        roleDetailsName.value = role.Role_Name
        roleDetailsID.value = role.Role_ID
        roleDetailsDesc.value = role.Role_Desc
    }).catch((err) => {
        console.log(err);
    });
})();
console.log(roleDetailsID)
console.log(roleDetailsID.value)
//SKILLS
const skillsList = ref([])

;(async() => {
    await getSkillsByRole(1)
    .then((skills) => {
        for(var skill of skills){
            //var skillDetails = [skill.Skill_id, skill.Skill_name, skill.Skill_desc]
            var skillDetails = {
                skill_id: skill.Skill_id,
                skill_name: skill.Skill_name,
                skill_desc: skill.skill_desc,
                courses_selected: []
            }
            skillsList.value.push(skillDetails) 
        }
        console.log(skillsList)
    }).catch((err) => {
        console.log(err);
    });
})();


//COURSES
const courseList = ref([])

function getAllCourses(skillID) {
    ;(async() => {
        await getCoursesBySkill(skillID)
        .then((courses) => {
            courseList.value = []
            for (var course of courses) {
                if (course.Course_Status == "Active") {
                    var courseDetails = {
                        course_name: course.Course_Name,
                        course_id: course.Course_ID,
                        course_desc: course.Course_Desc
                    }
                    courseList.value.push(courseDetails)
                }
            }
            console.log(courseList)
        }).catch((err) => {
            console.log(err);
        });
    })();
}

// skillID not working for some reason TT
const selectedCourses = ref([])
function addCourse(selectedCourses, skillID, skillsList) {
    console.log(skillID)
    for(var skill of skillsList){
        if (skill.skill_id === skillID) {
            for(var i=0; i<selectedCourses.length; i++){
                console.log(selectedCourses[i])
                skill.courses_selected.push(selectedCourses[i])
            }
            console.log(skill)
        }
    }
    while(selectedCourses.length > 0) {
        selectedCourses.pop();
    }
}

function deleteCourse(courseID, skillID, skillsList) {
    console.log(courseID)
    for(var skill of skillsList){
        if (skill.skill_id === skillID) {
            for( var i = 0; i < skill.courses_selected.length; i++){ 
                if ( skill.courses_selected[i] === courseID) { 
                    skill.courses_selected.splice(i, 1); 
                }
            }
            console.log(skill)
        }
    }
}
/*
function createLJ() {

}
*/

/*
//FAKE DATA
var LearningJourney = ref({
    jobRoleName: "Mechanical Engineeri",
    skills: {
        "skill1": {},
        "skill2": {},
        "skill3": {}
    }
})

const coursesList = ref({
    skillName: "skill",
    courses: {
        "course1": "course description 1",
        "course2": "course description 2",
        "course3": "course description 3",
        "course4": "course description 4",
        "course5": "course description 5"
    }
})

const skillListFake = ref(
    [1, "Facebook", "Duis consequat dui n"],
    [2, "UB04", "Phasellus in felis."],
    [3, "TMA", "In congue. Etiam jus"]
)
*/

</script>

<style scoped>
</style>