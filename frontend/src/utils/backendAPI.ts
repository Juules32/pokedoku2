import axios from "axios";

export async function getDailyData() {
    try {
        const response = await axios.get(`${import.meta.env.VITE_BACKEND_URL}/todaysPuzzle`);
        if (!response.data) {
            throw new Error('Response data not found');
        }
        return response.data
    } catch (error) {
        console.error(error)
    }
}
