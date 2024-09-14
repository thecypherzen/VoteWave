import { Link } from 'react-router-dom';

export default function NotFound(){
	return(
	<>
	<div>
		<h1>Sorry, we'd create that later.</h1>
		<p>For now let's take you back home.</p>
		<Link className="btn btnDark" to="/">Return Home</Link>
	</div>
	</>
	);
}