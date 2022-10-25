import { ref, reactive, computed } from "vue"
import { defineStore } from 'pinia'

export const useRoleStore = defineStore('role', () => {

    const role = reactive({
        roleName: '',
        roleID: '',
        roleDesc: '',
        coursesBySkillName: {}
        /*
        coursesBySkillName: {
            skillName1: {
                'skillID': '',
                'courses': {
                    courseName1: {courseDetail1},
                    courseName2: {courseDetail2}
                }
            },
        }
        */
    })

    const storeRole = (roleName, roleID, roleDesc, coursesBySkillName) => {
        role.roleName = roleName
        role.roleID = roleID
        role.roleDesc = roleDesc
        role.coursesBySkillName = coursesBySkillName
    }

    return {
        role,
        storeRole
    }

})
