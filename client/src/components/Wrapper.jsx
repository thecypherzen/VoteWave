/* Defines a  container structural component */
import '../styles/wrapper.css';

export default function Wrapper({clist=null, children}){
	let classes = "wrapper";
	if (clist)
	{
		const listLen = clist.length;
		for (let i = 0; i < listLen; i++){
			classes += ` ${clist[i]}`;
		}
	}
	return (
	<div className={classes}>{children}</div>)
}