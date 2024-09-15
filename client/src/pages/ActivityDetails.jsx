import { useLoaderData } from 'react-router-dom';
import axios from 'axios';
import ErrorPage from '../pages/ErrorPage';

export default function ActivityDetails(){
	const response = useLoaderData();
	console.log(response);
	if (response.error) {
		return (<ErrorPage error={response.data}/>)
	} else {
		const details = response.data;
		console.log(details);
		return (
		<>
		<p>Nothing to display...</p>
		</>);
	}
}

export async function loader({ params }){
	try {
		const res = await axios.get(
			`http://localhost:8082/api/v1/activities/${params.activityId}`)
		console.log(res);
		return {error: false, data: res.data};
	} catch (error) {
		return {error: true, data: error}
	}
}