const assert = require("assert");
const { segmentUrdish, mixUrdish } = require("../../app/src/main/assets/www/js/urdish.js");

const mixed = segmentUrdish("Boolean algebra یعنی بولین الجبرا deals with TRUE یعنی درست.");
assert.ok(mixed.length >= 3, "expected several script runs, got " + JSON.stringify(mixed));
assert.equal(mixed[0].l, "en");
assert.match(mixed[0].t, /Boolean/);
assert.ok(mixed.some((s) => s.l === "ur"), "must contain an Urdu span");
assert.ok(mixed.some((s) => s.l === "en" && /TRUE/.test(s.t)), "must keep English TRUE");

const onlyEn = segmentUrdish("AND gate output is 1");
assert.deepEqual(onlyEn, [{ l: "en", t: "AND gate output is 1" }]);

const onlyUr = segmentUrdish("خانہ خیال کو باندھتا ہے");
assert.equal(onlyUr.length, 1);
assert.equal(onlyUr[0].l, "ur");

const mixedTopic = mixUrdish(
  "Flexbox lays notes in a row.",
  "فلیکس باکس نوٹس کو قطار میں جماتا ہے۔"
);
assert.equal(mixedTopic[0].l, "en");
assert.equal(mixedTopic[mixedTopic.length - 1].l, "ur");
assert.ok(mixedTopic.some((s) => s.t.includes("یعنی") || s.l === "ur"));

assert.deepEqual(segmentUrdish(""), []);
console.log("urdish.test.js ok", mixed);
