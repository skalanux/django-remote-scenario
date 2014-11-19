var expect = chai.expect;

describe('Questions', function() {

    describe('Questions with no data', function() {

        before(function(runTests){
            $.get('http://localhost:8000/drs/demoapp/empty_scenario').done(runTests);
        });

        it('should get empty questions list', function(done) {
            (new Questions()).fetch().done(function (data) {
                expect(data).to.be.empty();
                done();
            }).fail(function(err){ done(err); });
        });
    });

    describe('Questions with data', function() {

        before(function(runTests){
            $.get('http://localhost:8000/drs/demoapp/scenario_1').done(runTests);
        });

        it('should get the questions list', function(done) {
            (new Questions()).fetch().done(function (data) {
                expect(data).to.have.length.of.at.least(4);
                done();
            }).fail(function(err){ done(err); });
        });
    });
});
