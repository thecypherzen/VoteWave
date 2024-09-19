import '../styles/errorpage.css';

export default function ErrorPage(data){
	return (
	<div className="error-content">
		<h1> Ouch!</h1>
		<p>{data.error.message}</p>
		<p><span>code: {data.error.code} </span> {
			console.log(data)
		}</p>
	</div>
	);
}