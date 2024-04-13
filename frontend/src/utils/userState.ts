import { reactive, ref } from 'vue'
import { getDailyData } from './backendAPI'

export const pokemonNames = reactive([
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ]
)

export const searchIndex = ref(-1)

export const dailyData = await getDailyData()

export const validPokemon = dailyData.validPokemon

export const rowCriteria = dailyData.rowCriteria

export const columnCriteria = dailyData.columnCriteria

console.log(dailyData)