import test from 'node:test';
import assert from 'node:assert/strict';
import {listOrders,createOrder,updateOrderStatus,listParts,savePart,resetMockData} from './mockService.js';

test.beforeEach(()=>resetMockData());

test('starts with sample repair orders',async()=>{const orders=await listOrders();assert.equal(orders.length,5);assert.equal(orders[0].id,'FF-1001');});
test('creates an order with a new number and history',async()=>{const order=await createOrder({customerName:'Test',phone:'',deviceType:'Laptop',deviceModel:'Test laptop',problem:'Will not start',receivedDate:'2026-10-22',status:'Received',technician:'',estimatedCost:null,notes:''});assert.equal(order.id,'FF-1006');assert.equal(order.history.length,1);});
test('records status changes',async()=>{const order=await updateOrderStatus('FF-1001','Repairing');assert.equal(order.status,'Repairing');assert.equal(order.history.at(-1).status,'Repairing');});
test('rejects negative part stock',async()=>{await assert.rejects(()=>savePart('',{name:'Test part',stock:-1,unitPrice:100}),/non-negative/);});
test('adds a spare part with the next ID',async()=>{const part=await savePart('',{name:'HDMI cable',stock:3,unitPrice:1200});assert.equal(part.id,'PT-05');assert.equal((await listParts()).length,5);});
test('rejects an unknown repair order',async()=>{await assert.rejects(()=>updateOrderStatus('FF-9999','Repairing'),/not found/);});