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
        <div class="flex justify-evenly gap-6 w-full">
            <button class="btn btn-outline btn-success w-2/6" @click="createRegis(skillsList, selectedCourses, registeredCourses, staffID, ljpsID)">Done</button>
            <button class="btn btn-outline btn-error w-2/6" @click="deleteLJ(staffID, jobRoleID, courseID, ljpsID)">Delete</button>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import { getLJs, getRoleByID, getSkillsByRole, getCoursesBySkill, getSkillIdByCourseName, getAllRegistrationNo } from "@/endpoint/endpoint.js";

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
const selectedCourses = ref([])
const toAddCourses = ref([])
const toDeleteCourses = ref([])

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
            selectedCourses.value.push(course[2])
    }

    courseID.value = registeredCourses.value[0][2] // for deleting LJ
    for (var a in registeredCourses.value) {
        var courseName = registeredCourses.value[a][2]
        const skillIDs = await getSkillIdByCourseName(courseName)
        var temp = 0
        for (var x in skillIDs) {
            for (var y in skillsIdList) {
                if (skillIDs[x] == skillsIdList[y]) {
                    if (temp == 0) {
                        registeredCourses2.value.push(skillIDs[x])
                        temp += 1
                    }
                }
            }
        }
    }

    const skills = await getSkillsByRole(jobRoleID.value)
    for (var skill of skills) {
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
                courses_available: courseList,
                courses_selected: regCourses
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


//COURSES
const coursesList = ref([])

function getAllCourses(skillID) {
    ;(async() => {
        await getCoursesBySkill(skillID)
        .then((courses) => {
            coursesList.value = []
            for (var course of courses) {
                if (course.Course_Status == "Active") {
                    var courseDetails = {
                        course_name: course.Course_Name,
                        course_id: course.Course_ID,
                        course_desc: course.Course_Desc
                    }
                    coursesList.value.push(courseDetails)
                }
            }
        }).catch((err) => {
            console.log(err);
        });
    })();
}

function temp(selectedCourses, registeredCourses) {
    //add new courses
    for (var sel_course_ID of selectedCourses) {
        var temp = 0
        for (var reg_course of registeredCourses) {
            var reg_course_ID = reg_course[2]
            if (sel_course_ID == reg_course_ID) {
                temp+=1
            }
        }
        if (temp == 0) {
            toAddCourses.value.push(sel_course_ID)
        }
    }
    //delete registered courses
    for (var reg_course of registeredCourses) {
        var reg_course_ID = reg_course[2]
        var temp = 0
        for (var sel_course_ID of selectedCourses) {
            if (sel_course_ID == reg_course_ID) {
                temp+=1
            }
        }
        if (temp == 0) {
            toDeleteCourses.value.push(reg_course_ID)
        }
    }
}

function createRegis(skillsList, selectedCourses, registeredCourses, staffID, ljpsID) {
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
            //add new courses
            for (var sel_course_ID of selectedCourses) {
                var temp = 0
                for (var reg_course of registeredCourses) {
                    var reg_course_ID = reg_course[2]
                    if (sel_course_ID == reg_course_ID) {
                        temp+=1
                    }
                }
                if (temp == 0) {
                    toAddCourses.value.push(sel_course_ID)
                }
            }
            //delete registered courses
            for (var reg_course of registeredCourses) {
                var reg_course_ID = reg_course[2]
                var temp = 0
                for (var sel_course_ID of selectedCourses) {
                    if (sel_course_ID == reg_course_ID) {
                        temp+=1
                    }
                }
                if (temp == 0) {
                    toDeleteCourses.value.push(reg_course_ID)
                }
            }           
            
            // add courses
            if (toAddCourses.value.length != 0) {
                //add registration
                for (var courseID of toAddCourses.value) {
                    addReg(regID, courseID, staffID)
                    regID+=1
                }
                //add course assignment
                for (var courseID of toAddCourses.value) {
                    addToLJ(courseID, ljpsID)
                }
            }
            
            // delete courses
            if (toDeleteCourses.value.length != 0) {
                for (var courseID of toDeleteCourses.value) {
                    deleteCourse(courseID, ljpsID, skillsList)
                }
            }

        
            //route to staff page
            alert('You have successfully modified your learning journey')
            router.push('/staff') 
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

function deleteCourse(courseID, ljpsID, skillsList) {
    var remainingSkillsNo = 0
    for (var skill of skillsList) {
        remainingSkillsNo += skill.courses_selected.length
        console.log(remainingSkillsNo)
    }
    if (remainingSkillsNo > 1) {
        ;(async() => {
            await fetch(`${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/DeLJAssignCourse/${courseID}/${ljpsID}`)
            .then((res) => {
                router.go(0)
            }).catch((err) => {
                console.log(err);
            });
        })();
    } else {
        alert('You need at least one course to continue.')
    }
}


function deleteLJ(staffID, roleID, courseID, ljpsID) {
    ;(async() => {
        await fetch(`${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/DeleteLJAssign/${staffID}/${roleID}/${courseID}/${ljpsID}`)
        .then((res) => {
            alert('You have successfully removed the learning journey.')
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