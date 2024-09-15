import '../styles/errorpage.css';

export default function ErrorPage({error}){
	return (
	<div className="error-content">
		<h1> Ouch!</h1>
		<p>{error.message}</p>
		<p><span>Response Text: </span> {
			error.response.data.error
		}</p>
	</div>
	);
}