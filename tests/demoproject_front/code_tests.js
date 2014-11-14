var expect = chai.expect;

describe('Questions', function() {
    
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