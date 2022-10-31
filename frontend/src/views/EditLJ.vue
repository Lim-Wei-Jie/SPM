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

                        <!-- modal pop up to delete course-->
                        <input type="checkbox" id="my-modal" class="modal-toggle" />
                        <div class="modal">
                            <div class="modal-box">
                                <h3 class="font-bold text-lg">{{ course }}</h3>
                                <div class="modal-action">
                                    <label for="my-modal" class="btn btn-outline btn-error" @click="deleteCourse(course, ljpsID)">Remove Course</label>
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
        <div class="flex justify-evenly gap-6 w-full">
            <button class="btn btn-outline btn-success w-2/6" @click="editLJ()">Done</button>
            <button class="btn btn-outline btn-error w-2/6" @click="deleteLJ(staffID, jobRoleID, courseID, ljpsID)">Delete</button>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { getLJs, getRoleByID, getSkillsByRole, getCoursesBySkill, getSkillIdByCourseName } from "@/endpoint/endpoint.js";

const router = useRouter()
function JobRolePage() {
    router.push('/staff/searchRole')
}
function HomePage() {
    router.push('/staff')
}

const props = defineProps({
    jobRoleID: {
        type: String
    },
    ljpsID: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleID } = toRefs(props)
const { ljpsID } = toRefs(props)


const staffID = '130003'
const courseList = ref()
const roleDetailsName = ref()
const roleDetailsDesc = ref()

const skillsIdList = []
;(async() => {
    await getSkillsByRole(jobRoleID.value)
    .then((skills) => {
        for(var skill of skills){
            skillsIdList.push(skill.Skill_ID)
        }
    }).catch((err) => {
        console.log(err);
    });
})();

// REGISTERED COURSES
const registeredCourses = ref([])
const registeredCourses2 = ref([])
const skillsList = ref([])
const courseID = ref()

;(async() => {
try {
    //SHOW JOB DETAILS
    const role = await getRoleByID(jobRoleID.value)
    roleDetailsName.value = role.Role_Name
    roleDetailsDesc.value = role.Role_Desc

    //SHOW REGISTERED COURSES
    const resA = await getLJs(staffID)
    for (var course of resA[jobRoleID.value]) {
            registeredCourses.value.push(course)
    }
    courseID.value = registeredCourses.value[0][2]
    for (var a in registeredCourses.value) {
        var courseName = registeredCourses.value[a][2]
        const skillIDs = await getSkillIdByCourseName(courseName)

        for (var x in skillsIdList) {
            for (var y in skillIDs) {
                if (skillsIdList[x] == skillIDs[y]) {
                    registeredCourses2.value.push(skillsIdList[x])
                }
            }
        }
    }

    const skills = await getSkillsByRole(jobRoleID.value)
    for (var skill of skills) {
        var regCourses = []
        for (let i = 0; i < registeredCourses2.value.length; i++) {
            if (registeredCourses2.value[i] == skill.Skill_ID) {
                regCourses.push(registeredCourses.value[i][2])
            }
        }
        var skillDetails = {
                skill_id: skill.Skill_ID,
                skill_name: skill.Skill_Name,
                skill_desc: skill.Skill_Desc,
                courses_selected: regCourses
            }
        skillsList.value.push(skillDetails) 
    }
}
catch(err) {

    console.log(err);
}
})();


//COURSES
const allCourseList = ref([])

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
                    allCourseList.value.push(courseDetails)
                }
            }
        }).catch((err) => {
            console.log(err);
        });
    })();
}

// skillID not working for some reason TT
const selectedCourses = ref([])
function addCourse(selectedCourses, skillID, skillsList) {
    for(var skill of skillsList){
        if (skill.skill_id === skillID) {
            for(var i=0; i<selectedCourses.length; i++){
                skill.courses_selected.push(selectedCourses[i])
            }
        }
    }
    while(selectedCourses.length > 0) {
        selectedCourses.pop();
    }
}

function deleteCourse(courseID, ljpsID) {
    ;(async() => {
        await fetch(`${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/DeLJAssignCourse/${courseID}/${ljpsID}`)
        .then((res) => {
            router.go(0)
        }).catch((err) => {
            console.log(err);
        });
    })();


}


function deleteLJ(staffID, roleID, courseID, ljpsID) {
    ;(async() => {
        await fetch(`${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/DeleteLJAssign/${staffID}/${roleID}/${courseID}/${ljpsID}`)
        .then((res) => {
            router.push('/staff')
        }).catch((err) => {
            console.log(err);
        });
    })();
}

function editLJ() {
    router.push({
        path: '/staff'
    })
}


</script>

<style scoped>
</style>