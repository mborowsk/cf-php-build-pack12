#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from datetime import datetime
from build_pack_utils import Builder
from compile_helpers import setup_htdocs_if_it_doesnt_exist


if __name__ == '__main__':
    (Builder()
        .configure()
            .default_config()
            .user_config()
            .done()
        .execute()
            .method(setup_htdocs_if_it_doesnt_exist)
        .install()
            .build_pack_utils()
            .extension()
                .from_build_pack('lib/{WEB_SERVER}')
                .done()
            .extension()
                .from_build_pack('lib/{PHP_VM}')
                .done()
            .extensions()
                .from_build_pack('extensions')
                .from_application('.extensions')
                .done()
            .done()
        .copy()
            .under('{BP_DIR}/bin')
            .into('{BUILD_DIR}/.bp/bin')
            .where_name_is('rewrite')
            .where_name_is('start')
            .any_true()
            .done()
        .save()
            .runtime_environment()
            .process_list()
            .done()
        .create_start_script()
            .using_process_manager()
            .write())
    print ''
    print '--------------------------------------------------------'
    print '|                     WARNING                          |'
    print '--------------------------------------------------------'
    print '|                                                      |'
    print '|          THIS VERSION HAS BEEN DEPRECATED.           |'
    print '|                                                      |'
    print '|             IT HAS BEEN REPLACED BY:                 |'
    print '|                    Version 1.3                       |'
    print '|                                                      |'
    print '|                 PLEASE UPGRADE!!                     |'
    print '|                                                      |'
    print '|     THIS VERSION MAY OR MAY NOT CONTINUE TO WORK!    |'
    print '|                                                      |'
    print '--------------------------------------------------------'
    print ''
    print 'Finished: [%s]' % datetime.now()
