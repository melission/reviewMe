
class ReviewDisplay extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            review: props.review
        };
    }

    render () {
        const review = this.state.review;

        return
        <div className="col mb-4">
            <div class=Name="card">
                <div className="card-body">
                    <h5 className="card-title">{review.book}
                        <strong>({review.rating})</strong>
                    </h5>
                    <h6 className="card-subtitle mb-2 text-muted">{ review.creator.email}</h6>
                    <p className="card-text"> { review.content }</p>
                </div>
                <div className="card-footer">
                    <a href={ '/books/' + review.book_id + '/' } className="card-link">View Book</a>
                </div>
            </div>
        </div>;
    }
}

class RecentReviews extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            reviews: [],
            currentUrl: props.url,
            nextUrl: null,
            previousUrl: null,
            loading: false
        };
    }
}