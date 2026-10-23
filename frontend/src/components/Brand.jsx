export default function Brand() {
  return (
    <a className="brand" href="/" onClick={(event) => event.preventDefault()}>
      <span className="brand-mark">h.</span>
      HobBob
    </a>
  );
}
