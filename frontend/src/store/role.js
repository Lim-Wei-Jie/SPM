import { ref, reactive, computed } from "vue"
import { defineStore } from 'pinia'

export const useRoleStore = defineStore('role', () => {

    const role = reactive({
        roleName: '',
        roleID: '',
        roleDesc: '',
        coursesBySkillName: {}
    })

    // // Getter using computed
    // const someComputedValue = computed(() =>
    //     role.value.roleName
    // )

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
