export default function ErrorPage({error, title}){
	return (
	<div>
		<h1> Oops! {title}</h1>
			{console.log(error)}
		<p></p>
	</div>
	);
}