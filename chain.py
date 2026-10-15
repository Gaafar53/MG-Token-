import hashlib, json, time, os

class MGChain:
    def __init__(self):
        self.chain_id = 7737005
        self.file = "mg_chain.json"
        self.genesis_hash = "6cb2386d58e2de1e2ac773ff31953505f06d64bec566beb5592016eb3b400ef"
        self.chain = []
        if os.path.exists(self.file):
            with open(self.file) as f:
                self.chain = json.load(f)
        if not self.chain:
            genesis = {
                "index": 0,
                "timestamp": int(time.time()),
                "data": f"MG-CHAIN:{self.chain_id}:{self.genesis_hash}",
                "prev_hash": "0"*64,
                "hash": self.genesis_hash,
                "wallet": "0x7564ac8dc5dcfa570a11dd3b21f579aee8e41982"
            }
            self.chain.append(genesis)
            self.save()
            print(f"✅ Genesis Created: {genesis['hash'][:20]}...")

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.chain, f, indent=2)

    def add(self, data):
        prev = self.chain[-1]
        block = {
            "index": len(self.chain),
            "timestamp": int(time.time()),
            "data": data,
            "prev_hash": prev["hash"],
        }
        block["hash"] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
        self.chain.append(block)
        self.save()
        print(f"⛏️ Block #{block['index']} Added: {block['hash'][:20]}...")

    def info(self):
        print(f"\n🌍 MG-CHAIN ID: {self.chain_id}")
        print(f"👛 Wallet: 0x7564ac8dc5dcfa570a11dd3b21f579aee8e41982")
        print(f"📦 Blocks: {len(self.chain)}")
        print(f"🔗 Genesis: {self.genesis_hash}\n")
        for b in self.chain[-5:]:
            print(f" #{b['index']} | {b['hash'][:16]}... | {b['data']}")

c = MGChain()
import sys
if len(sys.argv) > 1 and sys.argv[1] == "add":
    c.add(" ".join(sys.argv[2:]) if len(sys.argv)>2 else "Test TX")
else:
    c.info()
