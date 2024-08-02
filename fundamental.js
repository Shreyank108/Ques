// # def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
// #     # Merge the customers DataFrame with the orders DataFrame using a left join on 'id' and 'customerId'
// #     merged_df = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    
// #     # Use the 'customerId' column to create a boolean mask for customers who never placed any orders
// #     mask = merged_df['customerId'].isna()
    
// #     # Filter the rows using the boolean mask
// #     result_df = merged_df[mask]
    
// #     # Select only the 'name' column from the result DataFrame and rename it as 'Customers'
// #     result_df = result_df[['name']].rename(columns={'name': 'Customers'})
    
// #     return result_df 

// # var createHelloWorld = function() {
    
// #     return function(...args) {
// #         return 'Hello World'
// #     }
// # }


// #   const f = createHelloWorld()
// #   f() // "Hello 



// # let count =0   
// # count ++ 
// # return count 


// # var expect = function(val) {
// #     return {
// #         toBe: (val2) => {
// #             if(val === val2) return true;
// #             else throw new Error("Not Equal");
// #         },
// #         notToBe: (val2) => {
// #             if(val !== val2) return true;
// #             else throw new Error("Equal");
// #         }
// #     }
// # };


// #  let count = init;
// #     function increment(){
// #         count++;
// #         return count;
// #     }
// #     function decrement(){
// #         count--;
// #         return count;
// #     }
// #     function reset(){
// #         count = init;
// #         return count;
// #     }
// #     return { increment, decrement, reset };


// # /**
// #  * @param {number[]} arr
// #  * @param {Function} fn
// #  * @return {number[]}
// #  */
// # var map = function(arr, fn) {
// #   var mappedArray = [];
// #   for (var i = 0; i < arr.length; i++) {
// #     mappedArray.push(fn(arr[i], i));
// #   }
// #   return mappedArray;
// # }; 

// # var filter = function(arr, fn) {
// #     var filteredArr = [];
// #     for (var i = 0; i < arr.length; i++) {
// #         if (fn(arr[i], i)) {
// #             filteredArr.push(arr[i]);
// #         }
// #     }
// #     return filteredArr;
// # };



// # not for today 

// # return async function(...args) {
// #         return new Promise((resolve,reject) => {
// #             setTimeout(() => reject("Time Limit Exceeded"),t);
// #             fn(...args).then(resolve).catch(reject)
// #         })
// #     } 


// # Leetcode que no 2
// class Solution:
//     def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]: 

// dumyHead=ListNode(0) 
// tail=dumyHead  
// carry=0  

// while l1 is not None or l2 is not None or carry !=0 : 
//     digit1 = l1.val if  l1 is not None else 0    
//     digit2 = l2.val if l2 is not None else 0    
    
//     sum = carry + digit1 + digit2   
    
//     digit = sum%10   
//     carry = sum//10  
    
//     newNode = ListNode(digit) 
//     tail.next=newNode   
//     tail=tail.next 
    
//     l1=l1.next if l1 is not None else None   
//     l2=l2.next if l2 is not None else None   
    
// result =dumyHead.next   
// dumyHead.next=None   
// return result   
    
  

// /**
//  * @param {Array} arr
//  * @param {number} depth
//  * @return {Array}
//  */
// var flat = function (arr, depth) {
//  const stack = [...arr.map(item => [item, depth])];
//   const result = [];

//   while (stack.length > 0) {
//     const [item, depth] = stack.pop();

//     if (Array.isArray(item) && depth > 0) {
//       stack.push(...item.map(subItem => [subItem, depth - 1]));
//     } else {
//       result.push(item);
//     }
//   }

//   return result.reverse();
// };
// var compactObject = function(obj) {
//     if (obj === null) return null;
//     if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
//     if (typeof obj !== "object") return obj;
    
//     const compacted = {};
    
//     for (const key in obj) {
//         let value = compactObject(obj[key]);
//         if (Boolean(value)) compacted[key] = value;
//     }

//     return compacted;
// };
// class EventEmitter {
//   constructor() {
//     this.events = new Map();
//   }

//   subscribe(event, cb) {
//     if (!this.events.has(event)) {
//       this.events.set(event, []);
//     }

//     const listeners = this.events.get(event);
//     listeners.push(cb);

//     return {
//       unsubscribe: () => {
//         const index = listeners.indexOf(cb);
//         if (index !== -1) {
//           listeners.splice(index, 1);
//         }
//       }
//     };
//   }

//   emit(event, args = []) {
//     if (!this.events.has(event)) {
//       return [];
//     }

//     const listeners = this.events.get(event);
//     const results = [];

//     for (const listener of listeners) {
//       results.push(listener(...args));
//     }

//     return results;
//   }
// }