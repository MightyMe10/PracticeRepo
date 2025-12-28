const request = require('supertest');
const expect = require('chai').expect;
const app = require('../app');

describe('GET /', () => {
  it('should return Hello World', (done) => {
    request(app)
      .get('/')
      .expect(200)
      .end((err, res) => {
        if (err) return done(err);
        expect(res.text).to.equal('Hello World!');
        done();
      });
  });
});

describe('GET /health', () => {
  it('should return API status', (done) => {
    request(app)
      .get('/health')
      .expect(200)
      .end((err, res) => {
        if (err) return done(err);
        expect(res.body.status).to.equal('UP');
        done();
      });
  });
});

after(() => {
    app.close();
});
