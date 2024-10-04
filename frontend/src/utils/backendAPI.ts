import axios from "axios";

export async function getDailyData() {
    try {
        console.log("pee")
        const response = await axios.get(`${import.meta.env.VITE_BACKEND_URL}dailyData`);
        if (!response.data) {
            throw new Error('Response data not found');
        }
        return response.data
    } catch (error) {
        console.error(error)
    }
}
