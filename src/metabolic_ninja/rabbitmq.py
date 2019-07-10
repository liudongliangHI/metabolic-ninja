# Copyright (c) 2018, Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Functions to submit jobs through RabbitMQ."""

import json

import pika


def submit_job(**kwargs):
    """Submit a new job to the message queue."""
    message = json.dumps(kwargs)
    with pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    ) as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue="jobs", durable=True)
            channel.basic_publish(
                exchange="",
                routing_key="jobs",
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2  # Makes message persistent
                ),
            )
